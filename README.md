DocRead.ai – Intelligent Document Question Answering

Live: https://docread-ai.streamlit.app

Overview

DocRead.ai is an AI-powered document question-answering system built using Retrieval-Augmented Generation (RAG). The application allows users to upload PDF documents and interact with them using natural language queries.

The system processes the document, converts text into vector embeddings, stores them in a vector database, and retrieves the most relevant context to generate accurate answers using a language model.

This project demonstrates an end-to-end AI workflow including document ingestion, semantic search, vector databases, prompt engineering, and deployment using Streamlit.

Features

Upload and analyze PDF documents

Ask natural language questions about document content

Retrieval-Augmented Generation (RAG) architecture

Semantic search using vector embeddings

Fast similarity search with FAISS

Context-aware responses generated from document data

Interactive user interface built with Streamlit

Modular architecture for scalability

Cloud deployment ready

Tech Stack

Python

LangChain

FAISS Vector Database

Ollama / Local LLM

PyMuPDF

Streamlit

NumPy

pandas

Project Structure
DocRead.ai/
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

Text is extracted from the document

The text is split into smaller chunks

Each chunk is converted into vector embeddings

Embeddings are stored in a FAISS vector database

User queries are converted into embeddings

The most relevant document chunks are retrieved

The language model generates answers using the retrieved context

Deployment

The application can be deployed using:

Streamlit Community Cloud

Hugging Face Spaces

Docker containers

AWS / GCP / Azure

Author

Suraj Poddar

Data Science | Machine Learning | AI Applications

GitHub
https://github.com/surajpoddar13
