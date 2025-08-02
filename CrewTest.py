# Use a HuggingFace model for the agents
import os
from crewai import LLM, Crew, Agent, Task
# from crewai.llms import HuggingFaceLLM  # Import HuggingFaceLLM

def get_huggingface_token(token_file_path):
    with open(token_file_path, "r") as f:
        return f.read().strip()

token_path = os.path.join(os.path.dirname(__file__), "HFToken.txt")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = get_huggingface_token(token_path)
# Initialize LLM using Hugging Face model
llm = LLM(
    model="huggingface/mistralai/Mistral-7B-Instruct-v0.3",
    temperature=0.7,
    max_tokens=500
)

# Create agent
agent = Agent(
    role="Helpful Assistant",
    goal="Answer general questions clearly and concisely",
    backstory="You are an AI trained by Hugging Face to provide helpful answers.",
    llm=llm
)

# Create a task
task = Task(
    description="Explain the difference between supervised and unsupervised learning.",
    expected_output="A concise comparison of supervised and unsupervised learning with examples.",
    agent=agent
)

# Set up and run the crew
crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True
)

# Execute
result = crew.kickoff()
print("\nFinal Output:\n", result)