from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_classic.schema import Document

def split_documents(raw_docs):
    """
    Splits raw documents into smaller chunks for RAG.

    Args:
        raw_docs (list): List of dicts with 'text' and 'metadata'

    Returns:
        List[Document]: Chunks as LangChain Document objects
    """
    splitter=RecursiveCharacterTextSplitter(   # tries to split logically,not randomly,and better for code
        chunk_size=800,         # Max number of character per chunk
        chunk_overlap=150       # No of characters shared between consecutive chunks
    )  # This ensure continuity, context preservation and better answers

    documents=[]
    for doc in raw_docs: # loop through Raw documents
        splits = splitter.split_text(doc["text"]) # Takes the entire file content and then Breaks it into smaller chunks
        for chunk in splits:  # loops through each chunk i for chunk index and chunk is a actual text content
            documents.append(
                Document(
                    page_content=chunk, # Text
                    metadata=doc["metadata"]   # preserves source information
                )
            )
    return documents
