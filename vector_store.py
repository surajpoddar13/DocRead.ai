import faiss
from uuid import uuid4

from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_ollama import OllamaEmbeddings


class VectorStore:

    def __init__(self):

        self.embeddings = OllamaEmbeddings(
            model="nomic-embed-text"
        )

        dim = len(self.embeddings.embed_query("hello world"))

        index = faiss.IndexFlatL2(dim)

        self.vector_store = FAISS(
            embedding_function=self.embeddings,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={}
        )

    def add_docs(self, docs):

        ids = [str(uuid4()) for _ in docs]

        self.vector_store.add_documents(
            documents=docs,
            ids=ids
        )

    def search_docs(self, query, k=5):

        return self.vector_store.similarity_search(query, k=k)