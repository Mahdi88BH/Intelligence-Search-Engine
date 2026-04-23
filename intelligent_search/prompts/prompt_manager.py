import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class PromptManager:

    def __init__(self):
        self._prompts = {
            "query_enhancement": """
Generate 3 optimized search queries from:
{query}
Return Python list.
""",

            "summarization": """
Summarize the following content clearly:

{content}
""",

            "final_report": """
Create a professional report from these summaries:

{summaries}
"""
        }

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0.3,
            timeout=30,
            max_retries=3   
        )

    def get_prompt(self, key, **kwargs):
        return self._prompts[key].format(**kwargs)

    def get_llm(self):
        return self.llm
