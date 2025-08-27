from crewai import Agent
from utils.llm_factory import create_llm

manager_agent = Agent(
    role="Project Manager / Architect",
    goal="Design a clean and scalable architecture following SOLID principles.",
    backstory="You are an expert software architect and systems designer.",
    allow_delegation=True,
    verbose=True,
    llm=create_llm()
)
