from langchain.serpapi import SerpAPIWrapper
from langchain.agents import tool

@tool
def get_profile_url(text: str) -> str:
    """Search for a LinkedIn profile URL from text."""
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res