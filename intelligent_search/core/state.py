from pydantic import BaseModel
from typing import List, Dict


class GraphState(BaseModel):
    user_query: str
    enhanced_queries: List[str] = []
    urls: Dict[str, List[str]] = {}
    contents: Dict[str, List[str]] = {}
    summaries: Dict[str, List[str]] = {}
    final_report: str = ""