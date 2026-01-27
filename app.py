import streamlit as st
from vectorstore import create_vectorstore
from retriever import get_retriever
from llm import query_groq
from rag_pipeline import run_rag
from ingest import ingest_repository

st.set_page_config(page_title="Codebase RAG Assistant")

st.title("Codebase RAG Assistant")

#-------------------------------
# ingest repository
owner="pallets"
repo="flask"
documents=ingest_repository(owner,repo) # get our python code file

# create vectorstore and retriever
vectordb=create_vectorstore(documents)
retriever=get_retriever(vectordb)

# ASK a question
question=st.text_input("Ask a question about the codebase")

if st.button("Ask") and question:
    answer,docs=run_rag(retriever,query_groq,question)

    st.subheader("Answer")
    st.write(answer)

    st.expander("Sources")
    unique_sources = set(d.metadata['file_path'] for d in docs) #To avoid duplicate sources, deduplicate before displaying
    for src in unique_sources:
        st.write(src)