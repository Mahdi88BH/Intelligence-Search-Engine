from langchain_groq import ChatGroq
from core.config import Config


class LLMService:

    def __init__(self):
        self.fast = ChatGroq(
            model=Config.FAST_MODEL,
            api_key=Config.GROQ_API_KEY,
            temperature=0.3,
            timeout=30,
            max_retries=3
        )

        self.smart = ChatGroq(
            model=Config.FAST_MODEL,
            api_key=Config.GROQ_API_KEY,
            temperature=0.3,
            timeout=60,
            max_retries=3
        )

    def get(self, mode="fast"):
        return self.fast if mode == "fast" else self.smart