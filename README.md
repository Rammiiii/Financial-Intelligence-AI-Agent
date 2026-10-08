# 🚀 [Tips Hindawi](https://www.tipshindawi.com/) Internship (August–October) 2026

> 🎓 This project was built during the [ **Tips Hindawi** ](https://www.tipshindawi.com/) **Internship (August–October) 2026**.

## 👤 Participant

| Field            | Value                                       |
| ---------------- | ------------------------------------------- |
| Full Name        | Mohamed Mahmoud Ahmed Elramy                |
| Project Name     | Financial Intelligence AI Agent             |
| GitHub Username  | Rammiiii                                    |
| Internship Batch | August–October 2026                         |
| Training Program | Large Language Models (LLMs) Program        |
| Organization     | [**Edrak for Ai**](https://edrak4ai.com/en) |

---

# 📖 Project Overview

An autonomous, enterprise-grade Financial AI Agent powered by **Retrieval-Augmented Generation (RAG)**, **Qwen-3.8 LLMs via Groq**, and **FAISS Vector Store**.

## This system allows financial analysts and investors to upload complex financial documents in various formats (PDF, Word, Excel, CSV, TXT) and query them for precise metrics, CapEx trends, risk factors, and comparative analytics with executive-level summaries.

# ✨ Features

- Multi-Format Document Ingestion: Native parsing support for .pdf, .docx, .doc, .xlsx, .xls, .csv, and .txt files.
- Ultra-Fast Vector Retrieval: Powered by BAAI/bge-small-en-v1.5 embeddings running locally on CPU with FAISS.
- High-Performance Inference: Integrated with Groq LPU inference engine for lightning-fast LLM responses.
- Interactive UI: Built using Streamlit with real-time vector updating in a dedicated sidebar.

---

# 🛠️ Technologies Used

UI & Frontend: Streamlit

LLM Engine: Groq API (qwen/qwen3.8-27b / llama-3.3-70b-versatile)

RAG & Agent Framework: LangChain & LangChain Community

Embeddings: HuggingFace (BAAI/bge-small-en-v1.5) running locally on CPU

Vector Store: FAISS (Facebook AI Similarity Search)

Document Parsing & Ingestion: PyPDFLoader, Docx2txtLoader, Pandas, CSVLoader, TextLoader

Data Schemas: Pydantic

Environment Management: Python-dotenv

---

# ⚙️ Installation

- Python 3.10+
- 🔑 API Key Setup

This project requires a **Groq API Key** to run. 

1. Get your free API key from [Groq Console](https://console.groq.com/).
2. Create a `.env` file in the root directory of the project (you can copy `.env.example`).
3. Add your key as follows:
   ```env
   GROQ_API_KEY=gsk_your_actual_api_key_here

---

# 🚀 Usage

1. Document Ingestion (Sidebar)

- **Upload Files:** Navigate to the left sidebar and drag-and-drop or upload your financial files (`.pdf`, `.docx`, `.doc`, `.xlsx`, `.xls`, `.csv`, `.txt`).
- **Automatic Vectorization:** The system reads, chunks, generates embeddings using `BAAI/bge-small-en-v1.5`, and dynamically updates the local **FAISS Vector Index**. A success message will appear upon completion.

---

2. Formulating Analysis Requests
   Enter your financial question or comparison prompt in the main text box.

**Example Prompts:**

- **Metric Extraction:** _"What are the total net sales, CapEx figures, and gross margins for FY2024?"_
- **Risk & Trend Analysis:** _"Summarize the primary supply chain risk factors and investment priorities in AI infrastructure."_
- **Comparative Analysis:** _"Compare the Free Cash Flow (FCF) and liquidity positions across all uploaded company reports."_

---

3. Agent Execution & Output Review

- Click **Analyze Documents**.
- The agent retrieves relevant chunks from the FAISS database and utilizes the **Qwen 3.8 / Llama 3.3 LLM Engine** to synthesize a detailed financial analysis.
- **Output Structure:** Results are rendered directly in the Streamlit interface as executive summaries, detailed narrative insights, and structured Markdown comparison tables.

---

# 📸 Demo

<img width="1533" height="688" alt="Screenshot 2026-10-08 005552" src="https://github.com/user-attachments/assets/1d22af44-ada1-4b9e-8718-7df854ab1154" />


---

# 📈 Results

![

](<Screenshot 2026-10-08 010908-1.png>) ![

](<Screenshot 2026-10-08 010818-1.png>) ![

](<Screenshot 2026-10-08 010834-1.png>) ![

](<Screenshot 2026-10-08 010858-1.png>)

---

# 🔮 Future Improvements

- **Advanced Multi-Modal Document Parsing:** Integrate vision-language models (e.g., Unstructured.io or LLaVA) to extract structured tables, charts, and diagrams directly from complex 10-K SEC PDF filings.
- **Hybrid Search Retrieval (BM25 + Dense Vectors):** Combine FAISS dense vector search with sparse keyword search (BM25) to improve retrieval accuracy for exact financial ticker symbols, line-item codes, and specific monetary values.
- **SQL & Database Agent Integration:** Add text-to-SQL capabilities allowing the agent to run direct relational queries against enterprise financial databases (PostgreSQL/Snowflake) alongside unstructured document RAG.
- **Interactive Charting & Financial Data Visualization:** Integrate Plotly and Altair into Streamlit to automatically render interactive time-series line charts, revenue bar plots, and waterfall diagrams from extracted metrics.
- **Multi-Agent Orchestration (LangGraph):** Re-architect the agent pipeline into specialized sub-agents (e.g., _Data Retrieval Agent_, _Financial Ratios Specialist_, _Compliance & Audit Inspector_, _Report Writer_) with stateful human-in-the-loop review steps.

---

# 📚 About the Internship

This project was developed as part of the [**Tips Hindawi**](https://www.tipshindawi.com/) **Internship (August–October) 2026**, and it will be showcased on the official [Tips Hindawi](https://www.tipshindawi.com/) website.

[Tips Hindawi](https://www.tipshindawi.com/) is the internships department of [**Edrak for Ai**](https://edrak4ai.com/en), and the internship encourages participants to build real-world projects, apply practical skills, and showcase their work through GitHub.

For more information about the internship, training programs, and upcoming batches, visit the official [Tips Hindawi](https://www.tipshindawi.com/) website.

---

# 📄 License

This project is shared for educational and portfolio purposes.
