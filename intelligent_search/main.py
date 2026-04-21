from intelligent_search.graph.workflow import WorkflowBuilder

if __name__ == "__main__":
    app = WorkflowBuilder().build()
    result = app.invoke({"user_query": "Explain MLOps"})
    print(result["efficien_query"])