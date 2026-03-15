# DocRead.ai – Intelligent Document Question Answering
Live: https://docread.ai.streamlit.app

# Overview
DocRead.ai is an AI-powered document question-answering application built using Retrieval-Augmented Generation (RAG). The system allows users to upload PDF documents and ask natural language questions about their content.
The application extracts text from uploaded documents, converts the text into vector embeddings, stores them in a vector database, and retrieves relevant information to generate context-aware answers through an interactive Streamlit interface.

# Features
Upload and analyze PDF documents
Ask questions about document content
Retrieval-Augmented Generation (RAG) pipeline
Semantic search using vector embeddings
Fast similarity search using FAISS
Interactive web interface using Streamlit

# Tech Stack
Python
Streamlit
LangChain
FAISS
PyMuPDF
Ollama

# Installation
git clone https://github.com/surajpoddar13/DocRead.ai.git
cd DocRead.ai
pip install -r requirements.txt
Run Locally
streamlit run app.py

# Author

Suraj Poddar
GitHub: https://github.com/surajpoddar13
