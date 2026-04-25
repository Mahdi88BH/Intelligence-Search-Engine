from langgraph.graph import StateGraph, END
from core.state import GraphState
from agents.search_agent import SearchAgent
from agents.summarize_agent import SummarizeAgent
from agents.report_agent import ReportAgent


class Workflow:

    def __init__(self, container):
        self.c = container

    def fetch_urls(self, state):
        urls = {
            q: self.c.search_tool.run(q)
            for q in state.enhanced_queries
        }
        return {"urls": urls}

    def scrape(self, state):
        contents = {
            q: [self.c.scraper_tool.run(u) for u in urls]
            for q, urls in state.urls.items()
        }
        return {"contents": contents}

    def build(self):
        graph = StateGraph(GraphState)

        search_agent = SearchAgent(self.c.llm_service, self.c.prompt_service)
        summarize_agent = SummarizeAgent(self.c.llm_service, self.c.prompt_service)
        report_agent = ReportAgent(self.c.llm_service, self.c.prompt_service)

        graph.add_node("enhance", search_agent.run)
        graph.add_node("search", self.fetch_urls)
        graph.add_node("scrape", self.scrape)
        graph.add_node("summarize", summarize_agent.run)
        graph.add_node("report", report_agent.run)

        graph.set_entry_point("enhance")

        graph.add_edge("enhance", "search")
        graph.add_edge("search", "scrape")
        graph.add_edge("scrape", "summarize")
        graph.add_edge("summarize", "report")
        graph.add_edge("report", END)

        return graph.compile()