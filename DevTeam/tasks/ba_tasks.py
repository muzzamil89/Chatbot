from crewai import Task
from utils.file_io import read_file, write_file  # Assuming you already have these utils
from config import INPUT_FILE, REQUIREMENTS_FILE

def collect_requirements_task(agent):
    """
    Creates a Task for collecting requirements.

    1. Reads prompt from INPUT_FILE
    2. Builds a Task with instructions to rewrite as concise developer requirements
    3. Writes the generated output into REQUIREMENTS_FILE
    """

    # Step 1: Read input
    user_prompt = read_file(INPUT_FILE).strip()

    # Step 2: Build the task description
    task_description = (
        f"{user_prompt}. Create a simple, understandable write-up "
        f"that makes it easy for developers to understand the requirement. "
        f"Keep it short and precise."
    )

    # Step 3: Define a callback to write output into REQUIREMENTS_FILE
    def save_output(output: str):
        write_file(REQUIREMENTS_FILE, output)
        return f"Requirements saved to {REQUIREMENTS_FILE}"

    # Step 4: Return the Task object
    return Task(
        description=task_description,
        agent=agent,
        expected_output=f"Requirements saved to {REQUIREMENTS_FILE}",
        output_file=REQUIREMENTS_FILE,
        callback=save_output
    )