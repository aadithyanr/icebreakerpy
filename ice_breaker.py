from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain

info = input(
    "tell me someone you've always wanted to meet! i'll tell you about him/her: "
)

if __name__ == "__main__":
    print("hello open ai1")

    summary_template = """
        given info {info} of a person i want you to make a short summary of them & a few interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["info"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(info=info))
