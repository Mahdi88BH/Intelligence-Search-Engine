from core.container import Container
from graph.workflow import Workflow


def main():
    query = input("Enter your query: ")

    container = Container()
    app = Workflow(container).build()

    result = app.invoke({
        "user_query": query
    })

    print("\n===== FINAL REPORT =====\n")
    print(result["final_report"])


if __name__ == "__main__":
    main()