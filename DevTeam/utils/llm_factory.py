"""A factory for creating Language Model (LLM) instances for CrewAI agents."""
import os
from crewai import LLM
from config import GEMINI_API_KEY

def create_llm(llm_name: str = "gemini"):
    """
    Factory function to create and return an LLM instance based on the given name.
    Args:
        llm_name (str): The name of the LLM to create ('gemini' or 'ollama').
                        Defaults to 'gemini'.
    Returns:
        An instance of a CrewAI LLM wrapper.
    Raises:
        ValueError: If an unsupported llm_name is provided.
    """
    llm_name = llm_name.lower()
    if llm_name == "gemini":
        # Use the crewai.LLM wrapper and specify the model with the provider prefix
        return LLM(
            model="gemini/gemini-1.5-flash-latest", # Use a current and supported model
            api_key=GEMINI_API_KEY,
            temperature=0.2
        )
    elif llm_name == "ollama":
        ollama_model = os.getenv("OLLAMA_MODEL", "deepseek-coder:6.7b")
        ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        print(f"--- Using Ollama LLM: model='{ollama_model}' at '{ollama_base_url}' ---")
        return LLM(
            model=f"ollama/{ollama_model}", # e.g., ollama/deepseek-coder:6.7b
            base_url=ollama_base_url,
            temperature=0.7
        )
    else:
        raise ValueError(f"Unsupported LLM name: '{llm_name}'. Please choose 'gemini' or 'ollama'.")