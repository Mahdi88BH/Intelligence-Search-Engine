from typing import Dict
from intelligent_search.agents.base import BaseAgent
from dotenv import load_dotenv
from intelligent_search.prompts.prompt_manager import PromptManger
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

class SearchAgent(BaseAgent):
    
    def __init__(self, model_name: str):
        super().__init__(model_name)
        load_dotenv()
    
    

    def enhance(self, state: Dict[str, any]):
        prompt_manager = PromptManger()
        raw_prompt = prompt_manager.get_prompt('enhance_query')
        prompt = PromptTemplate.from_template(raw_prompt)
        formated_prompt = prompt.format(user_query=state['user_query'])
        llm_optimizer = ChatGoogleGenerativeAI(
            model=self.model_name
        )
        response = llm_optimizer.invoke(prompt)
        # update state
        return {'efficien_query': response}