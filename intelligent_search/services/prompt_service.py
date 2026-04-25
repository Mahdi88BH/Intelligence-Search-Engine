class PromptService:

    def __init__(self):
        self._prompts = {
            "enhance": """
You are an expert search query optimizer.

Generate EXACTLY 3 different, detailed search queries.

Rules:
- Each query must explore a different angle
- Be specific (not generic like "python")
- Return ONLY a valid Python list of 3 strings

User Query:
{query}

Example:
["what is python programming language explained",
"python tutorial for beginners step by step",
"advanced python use cases in data science"]
""",
            "summarize": "Summarize:\n{content}",
            "report": "Create report:\n{summaries}"
        }

    def get(self, key, **kwargs):
        return self._prompts[key].format(**kwargs)