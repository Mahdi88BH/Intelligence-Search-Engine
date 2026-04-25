from services.llm_service import LLMService
from services.prompt_service import PromptService
from tools.search_tool import SearchTool
from tools.scraper_tool import ScraperTool


class Container:

    def __init__(self):
        self.llm_service = LLMService()
        self.prompt_service = PromptService()
        self.search_tool = SearchTool()
        self.scraper_tool = ScraperTool()