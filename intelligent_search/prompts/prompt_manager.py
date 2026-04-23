import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

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

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            groq_api_key=os.getenv("api_groc"),
            temperature=0.3,
            max_retries=2
        )

    def get_prompt(self, key, **kwargs):
        return self._prompts[key].format(**kwargs)

    def get_llm(self):
        return self.llm
