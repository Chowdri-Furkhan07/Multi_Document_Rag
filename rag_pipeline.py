from pinecone import Pinecone
from langchain_community.embeddings import HuggingFaceEmbeddings
import requests
import re
from config import PINECONE_API_KEY, INDEX_NAME, GROQ_API_KEY

# ---------------- PINECONE ----------------
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

# ---------------- EMBEDDINGS ----------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------- RETRIEVE ----------------
def retrieve(query, department="ALL"):

    query_vec = embeddings.embed_query(query)

    filter_dict = {}

    if department != "ALL":
        filter_dict = {
            "department": department
        }

    results = index.query(
        vector=query_vec,
        top_k=10,
        include_metadata=True,
        filter=filter_dict
    )

    unique_docs = []
    seen = set()

    for match in results["matches"]:

        if "metadata" in match:

            text = match["metadata"]["text"]

            if text not in seen:
                seen.add(text)
                unique_docs.append(text)

    return unique_docs


# ---------------- DEPARTMENT EXTRACTION ----------------
def extract_departments(docs):

    departments = set()

    pattern = r"([A-Za-z ]+ Department)"

    for doc in docs:

        matches = re.findall(pattern, doc)

        for m in matches:
            departments.add(m.strip())

    if departments:
        return "\n".join(sorted(departments))

    return None


def is_department_query(query):

    q = query.lower()

    keywords = [
        "department",
        "departments",
        "list departments",
        "what departments",
        "which departments"
    ]

    return any(k in q for k in keywords)


# ---------------- SYSTEM EXTRACTION ----------------
def extract_systems(docs):

    systems = []

    for doc in docs:

        lines = doc.split("\n")

        capture = False

        for line in lines:

            clean_line = line.strip()

            # Start capturing
            if "core systems" in clean_line.lower():

                capture = True
                continue

            # Stop at next section
            if capture and any(
                section in clean_line.lower()
                for section in [
                    "security",
                    "policy",
                    "contact",
                    "department"
                ]
            ):
                break

            if capture and clean_line:

                systems.append(clean_line)

    if systems:

        unique_systems = list(dict.fromkeys(systems))

        return "\n".join(unique_systems)

    return None


def is_system_query(query):

    q = query.lower()

    keywords = [
        "system",
        "systems",
        "core systems",
        "what systems",
        "list systems",
        "systems used"
    ]

    return any(k in q for k in keywords)


# ---------------- LLM FALLBACK ----------------
def llm_answer(query, context):

    prompt = f"""
You are a company assistant.

RULES:

Use ONLY the provided context.
Return a clear structured answer.
Do NOT guess.

If information is not found, respond exactly:

Not found in company documents

Context:
{context}

Question:
{query}
"""

    res = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    return res.json()["choices"][0]["message"]["content"]


# ---------------- FINAL ANSWER ----------------
def answer(query, department="ALL"):

    docs = retrieve(query, department)

    if not docs:
        return "Not found in company documents"

    # Department logic
    if is_department_query(query):

        result = extract_departments(docs)

        if result:
            return result

    # System logic
    if is_system_query(query):

        result = extract_systems(docs)

        if result:
            return result

    # Default LLM fallback
    context = "\n\n".join(docs)

    return llm_answer(query, context)