from ddgs import DDGS
from tools.base import BaseTool
import time


class SearchTool(BaseTool):

    def run(self, query: str):
        urls = []

        print(f"🔎 Searching for: {query}")

        for attempt in range(3):
            try:
                with DDGS() as ddgs:
                    results = ddgs.text(
                        query,
                        region="wt-wt",
                        safesearch="off",
                        max_results=5
                    )

                    for r in results:
                        href = r.get("href")
                        if href and href.startswith("http"):
                            urls.append(href)

                if urls:
                    return urls[:3]

            except Exception as e:
                print(f"[Retry {attempt+1}] {e}")
                time.sleep(1)

        # ✅ Smart fallback: simplify query
        print("⚠️ No results → retry with simplified query")

        simple_query = " ".join(query.split()[:3])

        try:
            with DDGS() as ddgs:
                results = ddgs.text(simple_query, max_results=3)
                return [r["href"] for r in results if "href" in r]
        except:
            pass

        # ✅ FINAL fallback: return empty (clean design)
        print("❌ Search completely failed")
        return []