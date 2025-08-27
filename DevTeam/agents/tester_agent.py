"""Module defining the Tester agent."""
from crewai import Agent
from utils.llm_factory import create_llm

tester_agent = Agent(
    role="Software Quality Assurance Engineer",
    goal="Test the software for bugs, performance issues, and usability problems, then create a detailed bug report.",
    backstory=(
        "You are a meticulous QA Engineer with a knack for finding even the most "
        "obscure bugs. You are an expert in both automated and manual testing "
        "techniques. You are tasked with running the developed code, comparing its "
        "functionality against the requirements, and documenting any discrepancies "
        "in a `bug.txt` file. Your bug reports are clear, concise, and provide "
        "actionable steps to reproduce the issue. You will approve the project "
        "only when it is runnable and at least 85% of the requirements are met correctly."
    ),
    allow_delegation=False,
    verbose=True,
    llm=create_llm()
)
