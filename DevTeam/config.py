"""
Configuration settings for the AI Development Team project.

This file uses absolute paths derived from its own location to ensure
that file paths are resolved correctly, regardless of the current
working directory.
"""
import os
from dotenv import load_dotenv

# Get the absolute path of the directory containing this file (DevTeam)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv()

# --- API Keys ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --- Project Configuration ---
REVIEW_SCORE_THRESHOLD = 90

# --- File & Folder Paths (Absolute) ---
DELIVERABLES_DIR = os.path.join(BASE_DIR, "deliverable_project")
INPUT_FILE = os.path.join(DELIVERABLES_DIR, "input.txt") # Input file should be at the project root
REQUIREMENTS_FILE = os.path.join(DELIVERABLES_DIR, "requirements.txt")
ARCHITECTURE_FILE = os.path.join(DELIVERABLES_DIR, "architecture.txt")
BUG_FILE = os.path.join(DELIVERABLES_DIR, "bug.txt")
CODE_FOLDER = os.path.join(DELIVERABLES_DIR, "code/")
LOG_FILE = os.path.join(BASE_DIR, "devteam.log")