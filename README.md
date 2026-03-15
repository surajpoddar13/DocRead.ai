DocRead.ai – Intelligent Document Question Answering
Overview

DocRead.ai is an AI-powered document question-answering application built using Retrieval-Augmented Generation (RAG). The system allows users to upload PDF documents and ask natural language questions about their content.

The application extracts text from uploaded documents, converts the text into vector embeddings, stores them in a vector database, and retrieves relevant information to generate answers using a language model.

This project demonstrates a practical AI pipeline including document processing, semantic search, vector similarity retrieval, and an interactive Streamlit interface.

Features
Upload and analyze PDF documents
Ask questions about document content
Retrieval-Augmented Generation (RAG) pipeline
Semantic search using vector embeddings
Fast similarity search using FAISS
Context-based answers from documents

Interactive web interface built with Streamlit
Tech Stack
Python
Streamlit
LangChain
FAISS
PyMuPDF
Ollama

Project Structure
DocRead.ai
│
├── app.py
├── rag.py
├── vector_store.py
├── pdf_loader.py
├── requirements.txt
└── README.md

Installation
Clone the repository

git clone https://github.com/surajpoddar13/DocRead.ai.git
cd DocRead.ai

Install dependencies
pip install -r requirements.txt
Run Locally
streamlit run app.py

Open the browser at
http://localhost:8501

How It Works
User uploads a PDF document
Text is extracted from the document using PyMuPDF
The text is split into smaller chunks
Each chunk is converted into vector embeddings
Embeddings are stored in a FAISS vector database
User queries are converted into embeddings
The most relevant document chunks are retrieve
The language model generates answers using the retrieved context
Author
Suraj Poddar
