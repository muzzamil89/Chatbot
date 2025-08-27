"""Utility to parse the bug report file."""
import os
from config import BUG_FILE

def check_for_open_bugs() -> bool:
    """
    Checks the bug report file for an 'APPROVAL_STATUS: PASSED' line.
    Returns True if bugs are likely present, False if approved.
    """
    if not os.path.exists(BUG_FILE):
        # If tester doesn't create the file, assume it passed.
        return False

    with open(BUG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # If the approval line is not PASSED, we assume there are open bugs.
    if "APPROVAL_STATUS: PASSED" in content:
        return False

    return True
