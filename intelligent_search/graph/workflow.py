from langgraph.graph import StateGraph, END
from graph.state import GraphState

from agents.search_agent import SearchAgent
from agents.summarize_agent import SummarizeAgent
from agents.report_agent import ReportAgent

from tools.search_tool import SearchTool
from tools.scraper_tool import ScraperTool


class Workflow:

    def __init__(self):
        self.search_agent = SearchAgent()
        self.summarize_agent = SummarizeAgent()
        self.report_agent = ReportAgent()

        self.search_tool = SearchTool()
        self.scraper_tool = ScraperTool()

    def fetch_urls(self, state: dict):
        urls = {}
        for q in state["enhanced_queries"]:
            urls[q] = self.search_tool.run(q)
        return {"urls": urls}

    def scrape(self, state: dict):
        contents = {}
        for q, urls in state["urls"].items():
            contents[q] = [self.scraper_tool.run(url) for url in urls]
        return {"contents": contents}

    def build(self):
        graph = StateGraph(GraphState)

        graph.add_node("enhance", self.search_agent.run)
        graph.add_node("search", self.fetch_urls)
        graph.add_node("scrape", self.scrape)
        graph.add_node("summarize", self.summarize_agent.run)
        graph.add_node("report", self.report_agent.run)

        graph.set_entry_point("enhance")

        graph.add_edge("enhance", "search")
        graph.add_edge("search", "scrape")
        graph.add_edge("scrape", "summarize")
        graph.add_edge("summarize", "report")
        graph.add_edge("report", END)

        return graph.compile()