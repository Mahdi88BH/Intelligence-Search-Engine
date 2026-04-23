from typing import TypedDict, List, Dict


class GraphState(TypedDict):
    user_query: str
    enhanced_queries: List[str]
    urls: Dict[str, List[str]]
    contents: Dict[str, List[str]]
    summaries: Dict[str, List[str]]
    final_report: str