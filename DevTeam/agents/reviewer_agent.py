from crewai import Agent
from utils.llm_factory import create_llm

reviewer_agent = Agent(
    role="Code Reviewer",
    goal="Review the code, score it based on SOLID principles, and suggest improvements.",
    backstory="You are an experienced reviewer ensuring software quality.",
    allow_delegation=False,
    verbose=True,
    llm=create_llm()
)
