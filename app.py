import streamlit as st
from ingest import ingest_data
from rag_pipeline import answer

st.set_page_config(page_title="Company RAG System", layout="wide")

# ---------------- SESSION ----------------
if "chat" not in st.session_state:
    st.session_state.chat = []

st.title("🏢 Company Knowledge AI (RAG System)")

# ---------------- FILTERS ----------------

department = st.selectbox(
    "Department",
    ["ALL", "HR", "Finance", "IT"]
)

file_type = st.selectbox(
    "File Type",
    ["pdf", "docx", "csv", "web"]
)


# ---------------- FILE UPLOADER ----------------

files = st.file_uploader(
    "Upload Documents",
    type=["pdf", "docx", "csv", "html"],
    accept_multiple_files=True
)

# ---------------- INGEST ----------------
if files and st.button("Index Documents"):

    with st.spinner("Indexing..."):
        count = ingest_data(files, file_type, department)

    st.success(f"Indexed {count} files successfully")

# ---------------- CHAT ----------------
query = st.chat_input("Ask anything...")

if query:
    response = answer(query, department)

    st.session_state.chat.append(("user", query))
    st.session_state.chat.append(("ai", response))

    st.rerun()

# ---------------- DISPLAY ----------------
for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🏢 AI:** {msg}")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("### System Features")
    st.write("📄 PDF Support")
    st.write("📝 DOCX Support")
    st.write("📊 CSV Support")
    st.write("🌐 Web Support")

    st.markdown("### RAG Features")
    st.write("✔ Pinecone Vector DB")
    st.write("✔ Department Filtering")
    st.write("✔ LLM Answering")