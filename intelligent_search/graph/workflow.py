from intelligent_search.agents.search_agent import SearchAgent
from intelligent_search.graph.state import ResearchState
from langgraph.graph import StateGraph, START, END

class WorkflowBuilder:
    def __init__(self):
        self.agent = SearchAgent("gemini-1.5-flash")
    

    def build(self):
        graph = StateGraph(ResearchState)

        graph.add_node("refine_query", self.agent.enhance)
        graph.add_edge(START, "refine_query")

        return graph.compile()