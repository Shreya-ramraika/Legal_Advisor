import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
EMBED_MODEL = os.getenv("EMBED_MODEL")

FAITHFULNESS_THRESHOLD = float(os.getenv("FAITHFULNESS_THRESHOLD", 0.75))
MAX_EVAL_RETRIES = int(os.getenv("MAX_EVAL_RETRIES", 2))