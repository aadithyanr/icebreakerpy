from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """
    given the full name {name_of_person}, i want you to get me a link of that person's linkedin page. just reply back with only a url. no text pls.
    """
    tools_for_agent = [Tool(name="crawl google 4 linkedin profile page", func = "", description="useful to get linkedin urls")]
    
    