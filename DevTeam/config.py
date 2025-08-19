import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
#AIzaSyA1jUHs_C94OPg_JdUF6nolBM4QcLxKSKw
GEMINI_API_KEY = "#AIzaSyA1jUHs_C94OPg_JdUF6nolBM4QcLxKSKw" #os.getenv("GEMINI_API_KEY")

# Scoring Threshold
REVIEW_SCORE_THRESHOLD = 90

# File paths
INPUT_FILE = "deliverable_project/input.txt"
REVIEW_FILE = "deliverable_project/review.txt"
REQUIREMENTS_FILE = "deliverable_project/requirements.txt"
ARCHITECTURE_FILE = "deliverable_project/architecture.txt"
CODE_FILE = "deliverable_project/code.py"
REVIEW_REPORT_FILE = "deliverable_project/review_report.txt"
