
from .model import rerankerModel

def rerank_documents(query: str, documents: list[str]) -> list[str]:
    query_embedding = rerankerModel.model.encode(query)
    documents_embeddings = rerankerModel.model.encode(documents)

    # Calculate cosine similarity between query and documents
    similarities = [query_embedding @ document_embedding for document_embedding in documents_embeddings]

    # Sort documents by similarity
    reranked_documents = [document for _, document in sorted(zip(similarities, documents), reverse=True)]

    return reranked_documents