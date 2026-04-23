from agents.base import BaseAgent
from prompts.prompt_manager import PromptManager


class ReportAgent(BaseAgent):

    def __init__(self):
        self.pm = PromptManager()
        self.llm = self.pm.get_llm()

    def run(self, state: dict):

        all_summaries = ""

        for query, summaries in state["summaries"].items():
            all_summaries += f"\n\n### {query}\n"
            all_summaries += "\n".join(summaries)

        prompt = self.pm.get_prompt(
            "final_report",
            summaries=all_summaries
        )

        report = self.llm.invoke(prompt).content

        return {"final_report": report}