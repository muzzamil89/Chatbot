from crewai import Task, Agent
from utils.file_io import read_file
from config import INPUT_FILE, REQUIREMENTS_FILE

def collect_requirements_task(agent: Agent) -> Task:
    """
    Creates a Task for collecting requirements.

    1. Reads prompt from INPUT_FILE
    2. Builds a Task with instructions to rewrite as concise developer requirements
    3. The task output is automatically written to REQUIREMENTS_FILE.
    """

    user_prompt = read_file(INPUT_FILE).strip()

    task_description = (
        "Your task is to analyze the following user request and transform it into a "
        "detailed, actionable requirements document for the development team. "
        "The final output MUST be only the requirements document itself, without any "
        "preamble, questions, or conversational text.\n\n"
        "--- USER REQUEST ---\n"
        f"{user_prompt}\n"
        "--- END USER REQUEST ---\n\n"
        "Based on this request, create a requirements document that includes:\n"
        "1. A clear project goal.\n"
        "2. A list of key functional requirements (what the software should do).\n"
        "3. Any non-functional requirements implied by the request (e.g., performance, usability)."
    )

    return Task(
        description=task_description,
        agent=agent,
        expected_output=f"A detailed requirements document saved to {REQUIREMENTS_FILE}",
        output_file=REQUIREMENTS_FILE,
    )