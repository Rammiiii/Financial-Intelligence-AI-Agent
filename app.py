import os
import streamlit as st
from agent import analyze_finance, add_file_to_vectorstore

st.set_page_config(page_title="Financial Intelligence AI Agent", page_icon="📈", layout="wide")

st.title("📈 Financial Intelligence AI Agent")
st.write("Autonomous RAG agent for analyzing financial filings, earnings transcripts, and custom documents using Llama-3.3 and LangChain.")

# Sidebar for dynamic file uploads
with st.sidebar:
    st.header("📂 Upload Financial Documents")
    uploaded_file = st.file_uploader(
        "Upload a financial report (PDF, Word, Excel, CSV, TXT):", 
        type=["pdf", "txt", "csv", "docx", "doc", "xlsx", "xls"]
    )
    
    if uploaded_file is not None:
        os.makedirs("temp_uploads", exist_ok=True)
        file_path = os.path.join("temp_uploads", uploaded_file.name)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
            
        file_ext = uploaded_file.name.split(".")[-1].lower()
        
        with st.spinner(f"Processing `{uploaded_file.name}` and updating Vector Index..."):
            try:
                add_file_to_vectorstore(file_path, file_ext)
                st.success(f"Successfully indexed `{uploaded_file.name}`!")
            except Exception as e:
                st.error(f"Error indexing file: {e}")

# Query section
user_query = st.text_area(
    "Enter your financial query or analysis request:",
    placeholder="e.g., What are the primary revenue drivers, CapEx figures, and key risk factors mentioned in the uploaded file?",
    height=120
)

if st.button("Analyze Documents"):
    if user_query.strip():
        with st.spinner("Executing RAG retrieval and agent analysis..."):
            try:
                result = analyze_finance(user_query)
                st.success("Analysis Complete!")
                st.markdown("### 📊 Analysis Output:")
                st.write(result)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query before submitting.")