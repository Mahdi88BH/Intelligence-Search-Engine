import ast
from agents.base import BaseAgent


class SearchAgent(BaseAgent):

    def __init__(self, llm_service, prompt_service):
        self.llm = llm_service.get("fast")
        self.prompts = prompt_service

    def run(self, state):
        prompt = self.prompts.get("enhance", query=state.user_query)

        try:
            response = self.llm.invoke(prompt).content
            queries = ast.literal_eval(response)
        except:
            queries = [state.user_query]

        print("\n🔍 Enhanced Queries:", queries)

        return {"enhanced_queries": queries}