from ddgs import DDGS
from tools.base import BaseTool


class SearchTool(BaseTool):

    def run(self, query: str):
        urls = []

        try:
            with DDGS() as ddgs:
                results = ddgs.text(
                    query,
                    region="wt-wt",
                    safesearch="off",
                    max_results=5,
                    backend="duckduckgo"   
                )

                for r in results:
                    href = r.get("href")
                    if href and href.startswith("http"):
                        urls.append(href)

        except Exception as e:
            print(f"[SearchTool ERROR] {e}")
            return []

        return urls[:3]  # keep only 3