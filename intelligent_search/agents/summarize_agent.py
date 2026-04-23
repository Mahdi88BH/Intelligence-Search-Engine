from agents.base import BaseAgent
from prompts.prompt_manager import PromptManager


class SummarizeAgent(BaseAgent):

    def __init__(self):
        self.pm = PromptManager()
        self.llm = self.pm.get_llm()

    def run(self, state: dict):
        summaries = {}

        for query, contents in state["contents"].items():
            summaries[query] = []

            for content in contents:
                prompt = self.pm.get_prompt(
                    "summarization",
                    content=content
                )

                summary = self.llm.invoke(prompt).content
                summaries[query].append(summary)

        return {"summaries": summaries}