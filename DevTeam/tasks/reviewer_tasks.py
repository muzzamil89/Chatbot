"""Tasks for the Reviewer Agent."""
from typing import List
from crewai import Task, Agent
from config import REVIEW_REPORT_FILE, REVIEW_SCORE_THRESHOLD


def review_code_task(agent: Agent, context: List[Task]) -> Task:
    """Creates a task to review the implemented code.

    This task takes the implemented code from the context of a previous
    task and instructs the reviewer agent to score it and provide feedback.

    Args:
        agent: The agent responsible for the task.
        context: A list of tasks whose output will be used as context.

    Returns:
        A Task object.
    """
    return Task(
        description=f"""Review the Python code provided in the context.
The code is available as the output of the previous task.

Your review should focus on:
- Code quality and clarity
- Adherence to SOLID principles
- Correctness and functionality
- Potential bugs and security vulnerabilities

Provide a score out of 100. If the score is below {REVIEW_SCORE_THRESHOLD}, you MUST provide
detailed, actionable feedback and specific suggestions for improvement.

The final output must be a comprehensive review report, including the score and feedback.
""",
        agent=agent,
        context=context,
        expected_output=f"A comprehensive code review report, including a score and detailed feedback, saved to '{REVIEW_REPORT_FILE}'.",
        output_file=REVIEW_REPORT_FILE,
    )