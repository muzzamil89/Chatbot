from crewai import Task
from config import REQUIREMENTS_FILE, ARCHITECTURE_FILE
from utils.file_io import read_file, write_file

def design_architecture_task(agent):
    requirements = read_file(REQUIREMENTS_FILE)
    return Task(
        description=f"Create a system architecture based on the requirements:\n{requirements}",
        agent=agent,
        expected_output=f"Architecture saved to {ARCHITECTURE_FILE}",
        output_file=ARCHITECTURE_FILE,
        callback=lambda output: write_file(ARCHITECTURE_FILE, output)
    )
