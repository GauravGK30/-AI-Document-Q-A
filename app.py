# app.py
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from fastapi import FastAPI, UploadFile
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss, numpy as np, os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


embedder = SentenceTransformer("all-MiniLM-L6-v2")
index = None
documents = []

# -----------------------------
# Upload PDF
# -----------------------------
@app.post("/upload")
async def upload(file: UploadFile):
    global index, documents

    reader = PdfReader(file.file)
    documents = []

    for page in reader.pages:
        documents.append(page.extract_text())

    embeddings = embedder.encode(documents)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    return {"message": "Document indexed successfully"}

# -----------------------------
# Ask Question
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/ask")
def ask(query: str):
    if index is None:
        return {"error": "Upload document first"}

    query_emb = embedder.encode([query])
    _, ids = index.search(np.array(query_emb), k=3)

    context = "\n".join([documents[i] for i in ids[0]])

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{query}
"""

    response = model.generate_content(prompt)
    return {"answer": response.text}
