from crewai import Task
from config import CODE_FILE, REVIEW_REPORT_FILE, REVIEW_SCORE_THRESHOLD
from utils.file_io import read_file, write_file

def review_code_task(agent):
    code = read_file(CODE_FILE)
    return Task(
        description=f"Review the code and score it out of 100 based on SOLID principles. "
                    f"If score < {REVIEW_SCORE_THRESHOLD}, provide feedback for improvements.\n\n{code}",
        agent=agent,
        expected_output=f"Review report saved to {REVIEW_REPORT_FILE}",
        output_file=REVIEW_REPORT_FILE,
        callback=lambda output: write_file(REVIEW_REPORT_FILE, output)
    )
