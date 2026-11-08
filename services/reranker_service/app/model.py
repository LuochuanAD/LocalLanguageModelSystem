from sentence_transformers import SentenceTransformer
from config.loader import ConfigLoader
model_config, _ = ConfigLoader.get_service_config("reranker_service")

class RerankerModel:
    def __init__(self):
        print(f"Loading RerankerModel '{model_config.model_name}'...")
        self.model = SentenceTransformer(model_config.model_name)
        print("RerankerModel loaded successfully.")


rerankerModel = RerankerModel()
