# this function orchestrates the entire RAG process like retrieve ,Augment and generate
def run_rag(retriever,llm_fn,question):
    """
    Retrieve relevant chunks and query LLM (Groq).
    """

    docs=retriever.invoke(question) # question is converted to an embedding and then compare against vectors in Chromadb and then relevent chunks are returned 
    
    if not docs:
        return "No relevant context found.", []
    
    context="\n\n".join(
        f"File: {doc.metadata['file_path']}\n{doc.page_content}" 
        for doc in docs
    )    # Loops through retrieved chunks and add file path and code content

    answer=llm_fn(context,question)
    return answer,docs   # answer shown to user and docs is used for source display and debugging