from pinecone import Pinecone
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import PINECONE_API_KEY, INDEX_NAME
import uuid

from loaders import (
    load_pdf,
    load_docx,
    load_csv,
    load_web,
    clean_text
)

# ---------------- PINECONE ----------------
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

# ---------------- EMBEDDINGS ----------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------- SPLITTER ----------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    separators=[
        "\n\n",
        "\n",
        ". ",
        " "
    ]
)

# ---------------- INGEST ----------------
def ingest_data(files, file_type, department):

    vectors = []
    success_count = 0

    for file in files:

        try:

            print("Processing:", file.name)

            # AUTO DETECT FILE TYPE
            if file.name.endswith(".pdf"):

                docs = load_pdf(file)

            elif file.name.endswith(".docx"):

                docs = load_docx(file)

            elif file.name.endswith(".csv"):

                docs = load_csv(file)

            elif file.name.endswith(".html") or file.name.endswith(".htm"):

                docs = load_web(file)

            else:

                print("Unsupported file:", file.name)
                continue

            if not docs:

                print("No content:", file.name)
                continue

            # SPLIT
            chunks = splitter.split_documents(docs)

            for chunk in chunks:

                text = clean_text(
                    chunk.page_content
                )

                vector = embeddings.embed_documents(
                    [text]
                )[0]

                vectors.append({
                    "id": str(uuid.uuid4()),
                    "values": vector,
                    "metadata": {
                        "text": text,
                        "department": department,
                        "source": file.name
                    }
                })

            success_count += 1

        except Exception as e:

            print("FAILED FILE:", file.name)
            print(e)

    # Upload vectors
    if vectors:

        index.upsert(vectors=vectors)

    return success_count