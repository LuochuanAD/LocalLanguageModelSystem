from .model import embedding_model

def embed_query(text: str):
    return embedding_model.embed_query(text)

def embed_passage(text: str):
    return embedding_model.embed_passage(text)

def embed_batch(texts: list[str], is_query: bool = True):
    return embedding_model.embed_batch(texts, is_query)
