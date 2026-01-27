from langchain_chroma import Chroma
from splitter import split_documents
from langchain_huggingface import HuggingFaceEmbeddings

def create_vectorstore(documents,persist_directory="db"): # this function is used only once, when we are indexing the repository
    """
    Converts raw documents into embeddings and stores in ChromaDB.
    """
    chunks=split_documents(documents)
    embeddings=HuggingFaceEmbeddings(      # Convert text to numerical vectors (384 dimensions)
        model_name="sentence-transformers/all-MiniLM-L6-v2" # Convert text (sentences, paragraphs, code chunks) into dense numerical vectors (embeddings) that capture semantic meaning
    )
    # Takes each document then generates embeddings and stores them in ChromaDB
    vectordb=Chroma.from_documents(    
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory  # saved to chromadb 
    )

    #Writes vectors and metadata to the  disk
    return vectordb