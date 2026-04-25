class ReportAgent:

    def __init__(self, llm_service, prompt_service):
        self.llm = llm_service.get("fast")
        self.prompts = prompt_service

    def run(self, state):
        combined = str(state.summaries)

        prompt = self.prompts.get("report", summaries=combined)

        try:
            report = self.llm.invoke(prompt).content
        except:
            report = "Failed to generate report"

        return {"final_report": report}