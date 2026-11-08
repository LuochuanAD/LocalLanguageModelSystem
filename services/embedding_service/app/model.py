from sentence_transformers import SentenceTransformer
from config.loader import ConfigLoader
model_config, _ = ConfigLoader.get_service_config("embedding_service")

class EmbeddingModel:
    def __init__(self):
        print(f"Loading EmbeddingModel '{model_config.model_name}' on device '{model_config.device}'...")
        self.model = SentenceTransformer(model_config.model_name, device=model_config.device)
        print("EmbeddingModel loaded successfully.")

    def embed_query(self, text: str):
        text = "query: " + text
        return self.model.encode(text,normalize_embeddings=True).tolist()
    
    def embed_passage(self, text: str):
        text = "passage: " + text
        return self.model.encode(text,normalize_embeddings=True).tolist()
    
    def embed_batch(self, texts: list[str], is_query: bool = True):
        if is_query:
            prefixed_texts = ["query: " + text for text in texts]
        else:
            prefixed_texts = ["passage: " + text for text in texts]
        return self.model.encode(prefixed_texts, batch_size=32, normalize_embeddings=True).tolist()
    


embedding_model = EmbeddingModel()
