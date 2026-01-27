
# Creates a retriever from our vector database
def get_retriever(vectordb,k=5):    # top 5 relevent chunks to retrieve
    """
    Returns a retriever that fetches top-k relevant chunks.
    """

    return vectordb.as_retriever(
        search_type="similarity", # find vectors closest to the query vector,uses cosine similarity
        search_kwargs={"k":k} # controls context size and accuracy
    )