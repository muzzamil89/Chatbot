"""Utilities for file input and output operations."""
import os
import ast
import shutil
import time
from typing import Any, Dict

def read_file(path: str) -> str:
    """
    Reads the content of a file and returns it as a string.
    Raises an exception if the file is not found or is empty.
    """
    try:
        with open(path, "r", encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                raise ValueError(f"The file at '{path}' is empty. Application cannot proceed.")
            return content
    except FileNotFoundError:
        print(f"Error: The required file was not found at '{path}'.")
        raise
    except Exception as e:
        print(f"Error reading file at {path}: {e}")
        raise

def write_file(path: str, content: str):
    """Writes content to a file, creating parent directories if necessary."""
    try:
        dir_name = os.path.dirname(path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        with open(path, "w", encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file at {path}: {e}")

def write_folder_structure(base_path: str, structure: Dict[str, str], help_message: str = "", clean_directory: bool = True):
    """
    Creates or updates a folder structure and files from a dictionary.
    Includes a retry mechanism to handle file-locking issues.

    Args:
        clean_directory (bool): If True, the base_path is deleted before writing.
                                If False, files are updated or created in place.
    """
    if help_message:
        print(f"\n--- {help_message} ---")

    if clean_directory:
        # Clean the base directory with a retry mechanism
        if os.path.exists(base_path):
            for i in range(3):  # Retry up to 3 times
                try:
                    shutil.rmtree(base_path)
                    print(f"Cleaned base directory: {base_path}")
                    break
                except OSError as e:
                    print(f"Warning: Attempt {i+1} to clean directory failed: {e}. Retrying in 2 seconds...")
                    time.sleep(2)
            else: # This runs if the loop completes without a 'break'
                error_message = f"Could not clean base directory '{base_path}' after multiple attempts."
                print(f"Error: {error_message}")
                raise OSError(error_message)
        os.makedirs(base_path)
    elif not os.path.exists(base_path):
        os.makedirs(base_path)

    if not isinstance(structure, dict):
        print(f"Error: Expected a dictionary for folder structure, but got {type(structure)}.")
        return

    for file_path, content in structure.items():
        # Sanitize file_path to prevent writing outside the base_path
        safe_path = os.path.abspath(os.path.join(base_path, file_path))
        if not safe_path.startswith(os.path.abspath(base_path)):
            print(f"Security Warning: Skipping potentially malicious path '{file_path}'.")
            continue

        dir_name = os.path.dirname(safe_path)
        try:
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)
            with open(safe_path, 'w', encoding='utf-8') as f:
                f.write(str(content))
            print(f"Wrote file: {safe_path}")
        except Exception as e:
            error_message = f"Error creating directory or writing file {safe_path}: {e}"
            print(error_message)
            raise IOError(error_message) from e