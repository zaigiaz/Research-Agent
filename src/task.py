import hashlib
from pathlib import Path
import os

# main file where we build prompts for main and sub-agent

# TODO :: Latex Report Prompt
# TODO :: Generate Questions for Sub-Agents Prompt
# TODO :: System Startup Prompt, need tool-call example so we dont have parsing errors with pydantic
# TODO :: Tool-Calling Cleanup?

SYSTEM_PROMPT_PREFIX = r"""You're a Deep Research Agent meant to act as a search engine for academic purposes.
You have access to various search backends, pose questions and think in a clear and concise manner."""
QUESTION = "You will do deep research around {Prompt Question}" 
SETS = "Create {SUB_AGENT_NUMBER} Questions-Sets, each of these question-sets should be json arrays in a simple format with just the questions"


def read_template():
    """
    read a template file from the reports/ folder in project root
    """
    
def create_system_message(prefix: str, sets: str, prompt: str) -> str:
    """
    Create system prompt message for the main model and return
    """
    raise NotImplementedError 
    
def report_prompt() -> str:
    """
    prompt and settings for the org-mode report file and its syntax
    """
    raise NotImplementedError 

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
        UUID = hexdigest[:12]
        
        TASK_DIR = f"TASK--{UUID}"
        os.mkdir(TASK_DIR)
        os.mkdir(f"./{TASK_DIR}/search-agent-1/")
        os.mkdir(f"./{TASK_DIR}/search-agent-2/")
        Path(f"./{TASK_DIR}/report.org").touch()
        
        # TODO :: either have as file in data dir or specify in file?
        with open(f"./{TASK_DIR}/report.org", 'w', encoding="utf-8") as f:
            f.write("* Overview \n")
            f.close()

        return True

    except FileExistsError:
        print(f"Task directory {TASK_DIR} already exists")
        return False
    except Exception as e:
        print(f"Error creating task: {e}")
        return False
    

create_task("write a report on the instersection of topology and biology and how they relate")

