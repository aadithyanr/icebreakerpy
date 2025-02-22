from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from tools.tools import get_profile_url
from langchain.agents import initialize_agent, Tool, AgentType


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """
    given the full name {name_of_person}, i want you to get me a link of that person's linkedin page. just reply back with only a url. no text pls.
    """
    tools_for_agent = [
        Tool(
            name="crawl google 4 linkedin profile page",
            func=get_profile_url,
            description="useful to get linkedin urls",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linkedin_profile_url
