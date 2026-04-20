from sentence_transformers import SentenceTransformer
from config import EMBED_MODEL

def init_embedder():
    return SentenceTransformer(EMBED_MODEL)