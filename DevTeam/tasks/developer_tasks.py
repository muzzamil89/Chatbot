"""Tasks for the Developer Agent, focusing on high-quality, modular code generation."""
from typing import List, Dict
from crewai import Task, Agent
from pydantic import BaseModel, Field
from config import BUG_FILE, CODE_FOLDER
from utils.file_io import write_folder_structure

class CodeOutput(BaseModel):
    """Pydantic model for the developer agent's structured code output."""
    files: Dict[str, str] = Field(
        ...,
        description="A dictionary where keys are the relative file paths and values are the complete file contents."
    )

def implement_code_task(agent: Agent, context: List[Task]) -> Task:
    """
    Creates a task to implement code with a focus on quality and modularity.
    """
    return Task(
        description="""Based on the provided architecture design and requirements in the context, generate a complete, modular, and production-ready Python project.

        **Your Implementation MUST follow these rules:**
        1.  **Adhere to the Architecture**: Strictly follow the component design, data flow, and technology stack outlined in the architecture document.
        2.  **Modular Structure**: Create a logical directory structure (e.g., using a `src` directory). Separate features into their own modules.
        3.  **Complete Code**: Do not use placeholder comments like `# TODO: Implement logic here`. All functions and classes should have a complete and functional implementation.
        4.  **Include a README**: Generate a detailed `README.md` file that explains the project, how to set it up (mentioning `requirements.txt`), and how to run it with examples.
        5.  **Relative Paths**: All file paths in your output dictionary MUST be relative to the project's root (e.g., 'src/main.py').
        6.  **Ensure that the `src` folder contains an `__init__.py` file to make it a package.
        7.  **Code Quality**: Follow best practices for code quality, including meaningful variable names, proper error handling, and adherence to SOLID principles.
        8.  **Documentation**: Include docstrings for all classes and functions, explaining their purpose and usage.
        9.  **Testing**: If applicable, include unit tests for critical components in a `tests` directory.
        10. **Run the code and make sure there are no syntax errors or obvious bugs. If there are errors please show it. The code should be ready to run in a standard Python environment.**
        11. **In the readme file provide a sample input with commandline run and output for the code.**
        12. **If you are not able to run the code with sample input, then fix the code until you can run the code.**
        13. **Avoid ModuleNotFoundError: No module named 'src' and other syntax errors.**



        You MUST use the `CodeOutput` tool to format your final answer as a JSON object containing the complete file structure and code.
        """,
        agent=agent,
        context=context,
        expected_output=f"A JSON object containing the complete, modular, and well-documented code, which will be saved to '{CODE_FOLDER}'.",
        output_json=CodeOutput,
        callback=lambda output: write_folder_structure(CODE_FOLDER, output.json_dict['files'],
                                   help_message="Creating directory structure and files based on agent output")
    )

def fix_bugs_task(agent: Agent, context: List[Task]) -> Task:
    """
    Creates a task for the developer to fix bugs based on the manager's plan and tester's report.
    """
    return Task(
        description="""You must fix the bugs in the codebase. The manager's plan, the bug report, and the current code are all available in the context.
        Your task is to analyze the provided information and produce the complete, corrected version of the project.

        1.  Review the manager's instructions, the bug report from '{BUG_FILE}', and the current codebase provided in the context.
        2.  Focus on bugs with status 'NEW' or 'REOPENED'.
        3.  Implement the necessary code changes to fix the identified bugs, ensuring you maintain the project's modular structure.

        Your final output MUST be a JSON object using the `CodeOutput` tool, containing **ONLY the files that you have changed or added**.
        Do not include files that are unchanged from the original codebase.
        The file paths in the dictionary MUST be relative to the project root (e.g., 'src/main.py').
        """,
        agent=agent,
        context=context,
        expected_output=f"A JSON object containing the complete, corrected code, which will be saved to '{CODE_FOLDER}'.",
        output_json=CodeOutput,
        callback=lambda output: write_folder_structure(CODE_FOLDER, output.json_dict['files'], # noqa: E501
                                   help_message="Applying bug fixes and updating codebase",
                                   clean_directory=False) # Set to False to update in place
    )