# Use a HuggingFace model for the agents
import os
from crewai import LLM, Crew, Agent, Task
# from crewai.llms import HuggingFaceLLM


# Set your Hugging Face token if needed (uncomment and set path if required)
# def get_huggingface_token(token_file_path):
#     with open(token_file_path, "r") as f:
#         return f.read().strip()
# token_path = os.path.join(os.path.dirname(__file__), "HFToken.txt")
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = get_huggingface_token(token_path)

# Use CodeLlama 7B Instruct for code generation
# gllm = LLM(
#     model="deepseek-r1:8b",  # or the exact name you use in Ollama
#     provider="ollama",
#     temperature=0.7,
#     max_tokens=500
# )

ollama_llm = LLM(
    model="ollama/deepseek-r1:8b",  # Model format for CrewAI
    base_url="http://localhost:11434"  # Ollama's default local API endpoint
)

# Create agent
agent = Agent(
    role="Helpful Assistant",
    goal="Answer general questions clearly and concisely",
    backstory="You are an AI trained by Hugging Face CodeLlama to provide helpful answers, especially for code generation.",
    llm=ollama_llm
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