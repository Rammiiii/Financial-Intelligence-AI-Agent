import os
import re
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader, 
    TextLoader, 
    CSVLoader, 
    Docx2txtLoader
)
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage

# 1. Load Environment Variables
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(f"GROQ_API_KEY is missing. Please check your .env file at {env_path}")

# 2. Initialize Embeddings on CPU
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={'device': 'cpu'}
)

# 3. Load existing FAISS Vector Index or create fallback
INDEX_PATH = "data/financial_faiss_index"
if os.path.exists(INDEX_PATH):
    vectorstore = FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
else:
    vectorstore = FAISS.from_documents([Document(page_content="Initial Financial Index")], embeddings)

# 4. Dynamic File Loader for Multiple Formats (PDF, CSV, TXT, DOCX, XLSX)
def add_file_to_vectorstore(file_path: str, file_type: str):
    """Dynamically process and add uploaded financial documents to the FAISS Vector Index."""
    docs = []
    
    if file_type == "pdf":
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        
    elif file_type == "csv":
        loader = CSVLoader(file_path)
        docs = loader.load()
        
    elif file_type in ["docx", "doc"]:
        loader = Docx2txtLoader(file_path)
        docs = loader.load()
        
    elif file_type in ["xlsx", "xls"]:
        import pandas as pd
        excel_data = pd.read_excel(file_path, sheet_name=None)
        excel_texts = []
        for sheet_name, df in excel_data.items():
            text_content = f"Sheet: {sheet_name}\n" + df.to_string(index=False)
            excel_texts.append(Document(page_content=text_content, metadata={"source": file_path, "sheet": sheet_name}))
        docs = excel_texts
        
    else:
        loader = TextLoader(file_path, encoding='utf-8')
        docs = loader.load()
        
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    splits = text_splitter.split_documents(docs)
    
    vectorstore.add_documents(splits)

# 5. Direct Vector Retrieval Function
def retrieve_financial_docs(query: str) -> str:
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    docs = retriever.invoke(query)
    return "\n\n".join([d.page_content for d in docs])

# 6. Initialize Groq with Qwen 3.8 Model
llm = ChatGroq(
    temperature=0, 
    model_name="qwen/qwen3.8-27b",
    groq_api_key=api_key
)

SYSTEM_PROMPT = SystemMessage(content=(
    "You are an expert Financial Analyst. Analyze the retrieved financial context "
    "and provide a detailed, well-structured financial analysis with all exact numbers and metrics."
))

# 7. Main Execution Function
def analyze_finance(query: str) -> str:
    # 1. Fetch relevant financial chunks from vector database
    context = retrieve_financial_docs(query)
    
    # 2. Construct direct prompt to ensure full synthesis without raw tool tags
    messages = [
        SYSTEM_PROMPT,
        HumanMessage(content=(
            f"User Question: {query}\n\n"
            f"Retrieved Financial Context:\n{context}\n\n"
            "Based ONLY on the above financial context, provide a detailed financial report and analysis."
        ))
    ]
    
    response = llm.invoke(messages)
    return response.content