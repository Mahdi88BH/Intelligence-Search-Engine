import requests
from bs4 import BeautifulSoup
from tools.base import BaseTool


class ScraperTool(BaseTool):

    def run(self, url: str):
        try:
            res = requests.get(url, timeout=5)
            soup = BeautifulSoup(res.text, "html.parser")
            paragraphs = soup.find_all("p")
            text = " ".join([p.get_text() for p in paragraphs])
            return text[:3000]  # limit size
        except:
            return ""