from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType


def lookup(name: str) -> str:
    return "Linkedin Profile URL"
