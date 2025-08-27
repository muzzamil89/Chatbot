"""Task for an Interpreter Agent to process user requests."""
from crewai import Task, Agent
from utils.file_io import read_file
from config import INPUT_FILE, REQUIREMENTS_FILE

def interpret_user_request_task(agent: Agent) -> Task:
    """
    Creates a Task for interpreting the user's request.

    1. Reads the user's high-level request from INPUT_FILE.
    2. Builds a Task with instructions to convert it into a concise,
       AI-understandable prompt with clear requirements.
    3. The task output (the interpreted requirements) is automatically
       written to REQUIREMENTS_FILE.
    """
    user_prompt = read_file(INPUT_FILE).strip()

    task_description = (
        "You are an AI prompt engineer. Your task is to interpret the following "
        "high-level user request and convert it into a short, precise, and "
        "AI-understandable prompt that clearly outlines the project requirements. "
        "The output should be a structured document that a development team of AI agents "
        "can use to build the software.\n\n"
        "--- USER REQUEST ---\n"
        f"{user_prompt}\n"
        "--- END USER REQUEST ---\n\n"
        "Your final output MUST be only the refined requirements document, without any "
        "preamble, questions, or conversational text."
    )

    return Task(
        description=task_description,
        agent=agent,
        expected_output=f"A short and precise requirements document saved to {REQUIREMENTS_FILE}",
        output_file=REQUIREMENTS_FILE,
    )