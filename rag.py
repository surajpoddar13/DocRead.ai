from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

from pdf_loader import PdfLoader
from vector_store import VectorStore
from chunk_text import Chunker


class RAG:

    def __init__(self):

        self.prompt_template = """
You are an expert assistant.

Answer the question ONLY using the context below.

If the answer is not in the context say:
"I don't know."

Question:
{question}

Context:
{context}
"""

        self.prompt = PromptTemplate.from_template(self.prompt_template)

        self.llm = OllamaLLM(model="llama3.2:3b")

        self.loader = PdfLoader()
        self.chunker = Chunker()
        self.vector_store = VectorStore()


    def ingest(self, file_path):

        docs = self.loader.read_file(file_path)

        # safety check for bad PDFs
        if not docs:
            raise ValueError("No text could be extracted from the PDF.")

        chunks = self.chunker.chunk_docs(docs)

        self.vector_store.add_docs(chunks)


    def ask(self, query):

        docs = self.vector_store.search_docs(query)

        context = "\n\n".join([d.page_content for d in docs])

        chain = self.prompt | self.llm

        response = chain.invoke({
            "question": query,
            "context": context
        })

        return response