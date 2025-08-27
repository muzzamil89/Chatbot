from crewai import Crew
from agents.interpreter_agent import interpreter_agent
from agents.manager_agent import manager_agent
from agents.developer_agent import developer_agent
from agents.tester_agent import tester_agent  # New Agent
from tasks.interpreter_task import interpret_user_request_task
from tasks.manager_tasks import design_architecture_task, manage_bug_fixes_task
from tasks.developer_tasks import implement_code_task, fix_bugs_task
from tasks.tester_tasks import test_code_task
from utils.bug_parser import check_for_open_bugs

# Configuration for the bug fixing loop
MAX_FIX_ITERATIONS = 3

def run_pipeline():
    # Phase 1: Initial Development
    print("--- Phase 1: Initial Project Development ---")
    interpreter_task = interpret_user_request_task(interpreter_agent)
    manager_task = design_architecture_task(manager_agent, context=[interpreter_task])
    # Give the developer both the architecture and the original requirements for full context
    dev_task = implement_code_task(developer_agent, context=[manager_task, interpreter_task])

    # Create and run the initial development crew
    initial_crew = Crew(
        agents=[interpreter_agent, manager_agent, developer_agent],
        tasks=[interpreter_task, manager_task, dev_task]
    )
    initial_crew.kickoff()
    print("--- Initial development complete. Moving to testing and bug fixing phase. ---")

    # Phase 2: Iterative Testing and Bug Fixing Loop
    # for i in range(MAX_FIX_ITERATIONS):
    #     print(f"\n--- Bug Fixing Cycle: Iteration {i + 1} ---")

    #     # Step 1: Tester runs the code and reports bugs in bug.txt
    #     testing_task = test_code_task(tester_agent)
    #     testing_crew = Crew(agents=[tester_agent], tasks=[testing_task])
    #     testing_crew.kickoff()
    #     print("Testing complete. Checking for open bugs...")

    #     # Step 2: Check if there are any open bugs or if the project is approved
    #     if not check_for_open_bugs():
    #         print("\n--- Project Approved! ---")
    #         print("No open bugs found. The project meets the quality standards.")
    #         return  # Exit the pipeline successfully

    #     print("Open bugs found. Manager will review and assign fixes.")

    #     # Step 3: Manager reviews bugs and creates a plan for the developer
    #     # Pass the testing_task as context so the manager can see the bug report
    #     bug_management_task = manage_bug_fixes_task(manager_agent, context=[testing_task])
    #     management_crew = Crew(agents=[manager_agent], tasks=[bug_management_task])
    #     management_crew.kickoff()

    #     # Step 4: Developer fixes the bugs based on the manager's plan
    #     # Pass both the manager's plan and the original bug report for full context
    #     fixing_task = fix_bugs_task(developer_agent, context=[bug_management_task, testing_task])
    #     fixing_crew = Crew(agents=[developer_agent], tasks=[fixing_task])
    #     fixing_crew.kickoff()

    #     print(f"--- End of Iteration {i + 1}. Re-running tests. ---")

    # print("\n--- Max fix iterations reached! ---")
    print("The project may still contain open bugs. Exiting pipeline.")

if __name__ == "__main__":
    run_pipeline()
