import hashlib
from pathlib import Path
import os

# main file where we build prompts for main and sub-agent

# TODO :: Latex Report Prompt
# TODO :: Generate Questions for Sub-Agents Prompt
# TODO :: System Startup Prompt
# TODO :: Tool-Calling Cleanup?
# TODO :: create task folder, etc

SYSTEM_PROMPT_PREFIX = "You're a Deep Research Agent meant to act as a search engine for academic purposes. You have access to various search backends, pose questions and think in a clear and concise manner."
QUESTION = "You will do deep research around {Prompt Question}" 
SETS = "Create {SUB_AGENT_NUMBER} Questions-Sets, each of these question-sets should be json arrays in a simple format with just the questions"

def create_system_message(prefix: str, sets: str, prompt: str) -> str:
    print("hello")
    

def create_task(prompt) -> bool:
    """
    Create Folder for each Task that we will do
    with folders for each subagent and template for final report
    """
    try:
        prompt_to_bytes = str.encode(prompt)
        
        h = hashlib.new('sha256')
        h.update(prompt_to_bytes)
        hexdigest = h.hexdigest()
        UUID = hexdigest[:8]
        
        TASK_DIR = f"TASK--{UUID}"
        os.mkdir(TASK_DIR)
        os.mkdir(f"./{TASK_DIR}/sub-agent-1/")
        os.mkdir(f"./{TASK_DIR}/sub-agent-2/")
        Path(f"./{TASK_DIR}/report.org").touch()
        
        return True
    except FileExistsError:
        print(f"Task directory {TASK_DIR} already exists")
        return False
    except Exception as e:
        print(f"Error creating task: {e}")
        return False
    

create_task("hello")

