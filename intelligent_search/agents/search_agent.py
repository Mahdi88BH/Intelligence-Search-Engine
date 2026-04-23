import ast
from agents.base import BaseAgent
from prompts.prompt_manager import PromptManager


class SearchAgent(BaseAgent):

    def __init__(self):
        self.pm = PromptManager()
        self.llm = self.pm.get_llm()

    def run(self, state: dict):
        prompt = self.pm.get_prompt(
            "query_enhancement",
            query=state["user_query"]
        )

        response = self.llm.invoke(prompt).content

        try:
            queries = ast.literal_eval(response)
        except:
            queries = [state["user_query"]]

        # ✅ PRINT HERE (clean + readable)
        print("\n🔍 Enhanced Queries:")
        for i, q in enumerate(queries, 1):
            print(f"{i}. {q}")

        return {"enhanced_queries": queries}