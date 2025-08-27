"""Tasks for the Tester Agent."""
from crewai import Task, Agent
from utils.file_io import read_file, write_file # Import file_io functions
from config import CODE_FOLDER, INPUT_FILE, REQUIREMENTS_FILE, BUG_FILE

def test_code_task(agent: Agent) -> Task:
    """Creates a task to test the code and create/update a bug report."""
    return Task(
        description=f"""
        Your primary goal is to test the application code located in the '{CODE_FOLDER}' directory.
        You will simulate running the application and identify any bugs.
        You MUST use the `read_file` and `write_file` functions from `utils.file_io` for all file operations.

        **Testing Workflow:**

        1.  **Understand the Application**:
            -   First, read the `README.md` file located in the '{CODE_FOLDER}' directory using `read_file('{CODE_FOLDER}README.md')`. This file will tell you how to set up and run the application.
            -   You may also read other relevant code files in '{CODE_FOLDER}' using `read_file()` to understand the project structure and logic.
            -   Based on the `README.md` and the overall project context (from '{INPUT_FILE}' and '{REQUIREMENTS_FILE}'), understand the expected functionality.

        2.  **Simulate Execution and Identify Issues**:
            -   Simulate running the application as described in the `README.md`.
            -   Identify any discrepancies between the expected behavior (from '{INPUT_FILE}' and '{REQUIREMENTS_FILE}') and the simulated outcome.
            -   Look for errors, missing features, or incorrect outputs.
            -   If the application cannot be "run" or is fundamentally broken based on the `README.md` or code, document this as a critical bug.

        **Testing Workflow:**

        1.  **Check for existing bug report**: Look for '{BUG_FILE}'.
            -   If it exists, read it. You will be updating this file.
            -   If it does not exist, you will create a new one.

        3.  **Manage Bug Report ('{BUG_FILE}')**:
            -   **Check for existing bug report**: Attempt to read '{BUG_FILE}' using `read_file('{BUG_FILE}')`.
                -   If it exists, parse its content to understand previous bugs and their statuses.
                -   If `read_file` raises a `FileNotFoundError` or `ValueError` (empty file), assume no prior bug report exists and start fresh.

        2.  **Verify Fixed Bugs**: If the file exists, look for any bugs with the status 'FIXED'.
            -   For each 'FIXED' bug, re-run the test to verify the fix.
            -   If the bug is resolved, change its status to 'CLOSED'.
            -   If the bug is NOT resolved, change its status to 'REOPENED' and add a comment explaining why it's not fixed.

            -   **Update Existing Bugs**: For any bugs that are 'NEW' or 'REOPENED', re-evaluate them. If they are now fixed, change their status to 'FIXED'.

        3.  **Perform Full Regression Test**:
        4.  **Log New Bugs**:
            -   For any new issues you find, add them to the bug report.
            -   Each new bug entry must include:
                -   A unique Bug ID (e.g., BUG-001, continue the sequence if the file exists).
                -   A clear description of the issue.
                -   Steps to reproduce the bug.
                -   Severity (Critical, High, Medium, Low).
                -   Status, which must be 'NEW'.

        5.  **Update Approval Status**:
            -   After all testing, assess the overall project correctness.
            -   If the code is runnable (simulated) and meets at least 85% of the requirements (with no open 'Critical' or 'High' severity bugs), update the end of the file to be 'APPROVAL_STATUS: PASSED'.
            -   Otherwise, update it to 'APPROVAL_STATUS: FAILED'.

        Your final output MUST be the complete, updated content of the '{BUG_FILE}' file. Do not include any other text or conversational elements.
        """,
        agent=agent,
        expected_output=f"The complete, updated content of the '{BUG_FILE}' file.",
        callback=lambda output: write_file(BUG_FILE, output.raw)
    )
