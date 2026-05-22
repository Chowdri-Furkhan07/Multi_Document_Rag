# 🏢 Company Knowledge AI (RAG System)

## 📌 Project Overview

Company Knowledge AI is an enterprise-level **Retrieval-Augmented Generation (RAG)** system designed to intelligently search, retrieve, and generate answers from multi-format company documents using **LLMs, Pinecone Vector Database, and Semantic Search**.

The system supports:

- 📄 PDF Documents
- 📝 DOCX Files
- 📊 CSV Files
- 🌐 HTML / Web Documents

It enables employees to interact with organizational knowledge using natural language queries through a modern chat-based interface.

---

# 🚀 Features

- ✅ Multi-format document support
- ✅ Semantic Search using embeddings
- ✅ Pinecone Vector Database integration
- ✅ Department-based filtering (HR, Finance, IT)
- ✅ Groq LLaMA-powered intelligent responses
- ✅ Chat-based Streamlit UI
- ✅ Fast vector similarity retrieval
- ✅ Structured CSV understanding
- ✅ Web page content extraction
- ✅ Context-aware answer generation

---

# 🎯 Problem Statement

Large organizations store information in multiple formats such as:

- PDF reports
- DOCX documents
- CSV data sheets
- HTML/Web pages

Traditional search systems are:

- Keyword-based
- Slow and inefficient
- Not context-aware

Employees often struggle with:

- Searching across multiple document formats
- Extracting accurate information quickly
- Finding department-specific knowledge
- Understanding large unstructured datasets

This project solves the problem using an AI-powered RAG architecture with vector search and LLM-based reasoning.

---

# 🎯 Objectives

- Build a multi-format intelligent document assistant
- Support PDF, DOCX, CSV, and HTML files
- Implement Retrieval-Augmented Generation (RAG)
- Enable semantic search using vector embeddings
- Add department-wise filtering
- Integrate Groq LLaMA 3.1 model
- Provide a Streamlit chat interface
- Improve enterprise knowledge accessibility

---

# 🧠 Technologies Used

## Programming Language
- Python

## Frontend Framework
- Streamlit

## AI / NLP Framework
- LangChain

## Embedding Model
- Sentence Transformers
  - `all-MiniLM-L6-v2`

## Vector Database
- Pinecone

## LLM
- Groq API
  - `LLaMA 3.1 8B Instant`

## Document Processing Libraries
- PyPDF
- python-docx
- pandas
- BeautifulSoup

## Supporting Libraries
- requests
- python-dotenv
- re

---

# 🏗️ System Architecture

```text
User Uploads Documents (PDF / DOCX / CSV / HTML)
                ↓
        Document Loaders
                ↓
         Text Cleaning Module
                ↓
     Recursive Text Chunking
                ↓
   Embedding Generation (MiniLM)
                ↓
      Pinecone Vector Storage
                ↓
         User Query Input
                ↓
     Query Embedding Generation
                ↓
    Similarity Search (Top-K)
                ↓
   Metadata Filtering (Department)
                ↓
        Context Preparation
                ↓
      Groq LLaMA 3.1 Model
                ↓
         Final AI Response
```

---

# 📂 Project Structure

```bash
Company-RAG-System/
│
├── app.py
├── ingest.py
├── rag_pipeline.py
├── config.py
├── requirements.txt
├── README.md
│
├── documents/
│   ├── sample.pdf
│   ├── sample.docx
│   ├── sample.csv
│
└── assets/
    └── architecture.png
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Chowdri-Furkhan07/Multi_Document_Rag.git

cd Multi_Document_Rag.git
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
PINECONE_API_KEY=your_pinecone_api_key

INDEX_NAME=company-rag-index

GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 💬 Streamlit UI Features

- 📤 Upload multiple documents
- 🏢 Department filtering
- 📄 File type selection
- 💬 Chat interface
- ⚡ Real-time responses
- 📚 Chat history support

---

# 🧩 System Modules

## 1️⃣ Document Ingestion Module

Supports:

- PDF
- DOCX
- CSV
- HTML/Web pages

---

## 2️⃣ Data Cleaning Module

- Removes noise
- Cleans whitespace
- Standardizes formatting

---

## 3️⃣ Chunking Module

- Recursive text splitting
- Improves retrieval accuracy

---

## 4️⃣ Embedding Module

Uses:

```python
all-MiniLM-L6-v2
```

to convert text into vector embeddings.

---

## 5️⃣ Vector Storage Module

- Stores embeddings in Pinecone
- Adds metadata:
  - Department
  - Source file

---

## 6️⃣ Retrieval Module

- Converts query into embeddings
- Performs similarity search
- Applies metadata filtering

---

## 7️⃣ LLM Answer Generation Module

Uses:

- Groq API
- LLaMA 3.1 8B Instant

Features:

- Context-aware answers
- Hallucination reduction
- Structured responses

---

## 8️⃣ Streamlit UI Module

Provides:

- Chat interface
- Upload system
- Sidebar information
- Filters

---

# 📊 Output

The system provides:

- ✅ Accurate context-based answers
- ✅ Department-specific responses
- ✅ Intelligent semantic retrieval
- ✅ LLM-generated explanations
- ✅ Fast real-time interaction
- ✅ Chat history tracking

---

# 🧪 Example Queries

```text
What are the HR policies?

List all departments.

What core systems are used in Finance?

Show IT department security policies.
```

---

# 📌 Applications

- Enterprise Knowledge Management
- HR Policy Assistant
- IT Support Automation
- Financial Report Analysis
- Internal Company Chatbot
- Intelligent Document Search
- Customer Support Automation

---

# 🔮 Future Enhancements

- Multi-user authentication
- Role-Based Access Control (RBAC)
- Analytics dashboard
- Voice-enabled querying
- Hybrid search
- Cloud deployment (AWS/Azure/GCP)
- Fine-tuned enterprise LLMs
- Real-time document synchronization

---

# 📈 Advantages

- Faster information retrieval
- Improved enterprise productivity
- Accurate semantic understanding
- Reduced manual searching
- Context-aware intelligent answers

---

# 🖼️ Screenshots

## Chat Interface
<img width="940" height="454" alt="image" src="https://github.com/user-attachments/assets/b91da594-b290-4974-aa64-f520c77f73d9" />

---

# 📚 Tech Highlights

| Technology | Purpose |
|---|---|
| LangChain | RAG Pipeline |
| Pinecone | Vector Database |
| MiniLM | Embedding Generation |
| Groq LLaMA 3.1 | Answer Generation |
| Streamlit | Frontend UI |

---

# 👨‍💻 Author

** Chowdri Furkhan**

- Data Analyst
- AI/ML Enthusiast

---

# ⭐ Conclusion

The Company RAG System is a powerful enterprise AI solution that combines:

- Multi-format document intelligence
- Vector databases
- Semantic search
- Large Language Models

to create an intelligent company knowledge assistant capable of delivering fast, accurate, and context-aware answers.

---
