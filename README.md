📄 AI Document Q&A

This project lets you upload a PDF and ask questions about it.
It uses AI embeddings + semantic search to find relevant content from the document and then generates accurate answers using Google Gemini.

Built as a simple, practical demo of AI-powered document understanding.

 Features

Upload any PDF document

Ask natural language questions

Semantic search using sentence embeddings

AI-generated answers based only on document content

Clean UI with FastAPI + Jinja templates

 Tech Stack

FastAPI

Sentence Transformers

FAISS (Vector Search)

Google Gemini API

Python

 How to Run
pip install -r requirements.txt
uvicorn app:app --reload


Create a .env file:

GEMINI_API_KEY=your_api_key_here


Open in browser:
👉 http://127.0.0.1:8000

 Use Case

Helpful for:

Reading large PDFs quickly

Academic notes & research papers

AI document search demos

👤 Author

Gaurav Kankuse
