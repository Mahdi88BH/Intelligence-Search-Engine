from typing import TypedDict, List, Optional

class QueryOptimization(TypedDict):
    user_query: str
    # enhanced_queries: List[str]
    enhanced_queries: str


class ResearchState(TypedDict):
    user_query: str
    queries_optimization: Optional[QueryOptimization]