from crewai import LLM
from config import GEMINI_API_KEY

def create_gemini_llm(llmname="gemini-pro"):
    if(llmname == "ollama"):
        return create_ollama_llm() 
    return LLM(
        model="gemini-pro",
        api_key=GEMINI_API_KEY,
        temperature=0.2
    )

def create_ollama_llm():
    return LLM(
        model="ollama/deepseek-r1:8b",  # Model format for CrewAI
        base_url="http://localhost:11434",  # Ollama's default local API endpoint
        stream=True,
        temperature=0.7,
        max_tokens=500
    )
