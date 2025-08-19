from crewai import Task
from config import ARCHITECTURE_FILE, CODE_FILE
from utils.file_io import read_file, write_file

def implement_code_task(agent):
    architecture = read_file(ARCHITECTURE_FILE)
    return Task(
        description=f"Write Python code following the architecture:\n{architecture}",
        agent=agent,
        expected_output=f"Code saved to {CODE_FILE}",
        output_file=CODE_FILE,
        callback=lambda output: write_file(CODE_FILE, output)
    )

def fix_code_task(agent, feedback):
    return Task(
        description=f"Update the code based on the following review feedback:\n{feedback}",
        agent=agent,
        expected_output=f"Updated code saved to {CODE_FILE}",
        output_file=CODE_FILE,
        callback=lambda output: write_file(CODE_FILE, output)
    )
