from .client import client

COLLECTION_NAME = "documents"

def upset_vectors(vectors):
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=vectors
    )

def search_vectors(vector, top_k=5):
    search_result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=top_k
    )
    return search_result

