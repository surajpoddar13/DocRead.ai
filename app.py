import streamlit as st
from rag import RAG
import tempfile

st.set_page_config(page_title="Ask Your Document", layout="wide")

# cache RAG instance
@st.cache_resource
def load_rag():
    return RAG()

rag = load_rag()

# session state to track document processing
if "doc_processed" not in st.session_state:
    st.session_state.doc_processed = False

st.title("📚 Ask Your Document")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None and not st.session_state.doc_processed:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        file_path = tmp_file.name

    if st.button("Process Document"):

        with st.spinner("Processing document..."):
            rag.ingest(file_path)

        st.session_state.doc_processed = True
        st.success("Document indexed successfully!")

# Ask questions AFTER document processed
if st.session_state.doc_processed:

    query = st.text_input("Ask a question about your document")

    if query:
        with st.spinner("Thinking..."):
            answer = rag.ask(query)

        st.write("### Answer")
        st.write(answer)