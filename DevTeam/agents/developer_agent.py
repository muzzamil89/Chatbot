from crewai import Agent
from utils.llm_factory import create_gemini_llm

developer_agent = Agent(
    role="Senior Developer",
    goal="Implement the project requirements in code following the provided architecture.",
    backstory="You are a seasoned developer with expertise in Python and best practices.",
    allow_delegation=False,
    verbose=True,
    llm=create_gemini_llm("ollama")
)
