from graph.workflow import Workflow


def main():
    query = input("Enter your query: ")

    app = Workflow().build()

    result = app.invoke({
        "user_query": query

    })

    print("\n===== FINAL REPORT =====\n")
    print(result["final_report"])

    # save report
    with open("report.txt", "w") as f:
        f.write(result["final_report"])


if __name__ == "__main__":
    main()