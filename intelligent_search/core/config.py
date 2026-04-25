import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    FAST_MODEL = os.getenv("FAST_MODEL", "llama-3.3-70b-versatile")
    #SMART_MODEL = os.getenv("SMART_MODEL", "gemini-2.5-pro")

    # llama-3.3-70b-versatile