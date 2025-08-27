from crewai import Agent
from utils.llm_factory import create_llm

ba_agent = Agent(
    role="Business Analyst",
    goal="Gather complete and clear project requirements from the client.",
    backstory="You are skilled at asking the right questions to clarify any ambiguities.",
    allow_delegation=False,
    verbose=True,
    llm=create_llm()
)
