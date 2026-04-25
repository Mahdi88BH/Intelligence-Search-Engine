class SummarizeAgent:

    def __init__(self, llm_service, prompt_service):
        self.llm = llm_service.get("fast")
        self.prompts = prompt_service

    def run(self, state):
        summaries = {}

        for q, contents in state.contents.items():
            summaries[q] = []

            for c in contents:
                prompt = self.prompts.get("summarize", content=c)

                try:
                    summary = self.llm.invoke(prompt).content
                except:
                    summary = "Error"

                summaries[q].append(summary)

        return {"summaries": summaries}