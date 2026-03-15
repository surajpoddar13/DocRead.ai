from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class Chunker:

    def __init__(self, chunk_size=1500, chunk_overlap=200):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def chunk_docs(self, docs):

        list_of_docs = []

        for doc in docs:

            chunks = self.text_splitter.split_text(doc.page_content)

            for chunk in chunks:
                list_of_docs.append(
                    Document(
                        page_content=chunk,
                        metadata=doc.metadata
                    )
                )

        return list_of_docs