from crewai import Crew
from agents.ba_agent import ba_agent
from agents.manager_agent import manager_agent
from agents.developer_agent import developer_agent
from agents.reviewer_agent import reviewer_agent
from tasks.ba_tasks import collect_requirements_task
from tasks.manager_tasks import design_architecture_task
from tasks.developer_tasks import implement_code_task, fix_code_task
from tasks.reviewer_tasks import review_code_task
from config import REVIEW_SCORE_THRESHOLD
from utils.file_io import read_file

def run_pipeline():
    # Step 1: Collect requirements
    ba_task = collect_requirements_task(ba_agent)

    # Step 2: Design architecture
    manager_task = design_architecture_task(manager_agent)

    # Step 3: Implement code
    dev_task = implement_code_task(developer_agent)

    # Step 4: Review code
    review_task = review_code_task(reviewer_agent)

    crew = Crew(
        agents=[ba_agent, manager_agent, developer_agent, reviewer_agent],
        tasks=[ba_task, manager_task, dev_task, review_task]
    )

    crew.kickoff()

    # Step 5: Check score and possibly fix
    review_output = read_file("deliverable_project/review_report.txt")
    try:
        score_line = [line for line in review_output.splitlines() if "score" in line.lower()][0]
        score = int("".join([c for c in score_line if c.isdigit()]))
    except:
        score = 0

    if score < REVIEW_SCORE_THRESHOLD:
        print(f"Score {score} is below threshold. Sending back to developer for fixes...")
        fix_task = fix_code_task(developer_agent, review_output)
        Crew(agents=[developer_agent], tasks=[fix_task]).kickoff()
    else:
        print(f"Score {score} meets or exceeds threshold. Project delivery complete.")

if __name__ == "__main__":
    run_pipeline()
