from llama_cpp import Llama
from contextlib import contextmanager
import os
import sys
import config as cfg

# TODO :: rich interface?
# TODO :: sub-agents with llama_pool

def init_model(config: dict):
    """
    Basic Model Init, read params from json config later
    """
    cfg.logger.info("Loading llama.cpp model")
    with llama_model_log():
        llm = Llama(
            model_path = config.get('model'),
            n_ctx      = config.get('n_ctx'),
            verbose    = True,
        )
    
    cfg.logger.info("llama.cpp model loaded succesfully")
    return llm

# TODO :: have this log in the dedicated <Task> Folder and make sure we get full output instead of cutoff
def llm_response(llm_backend, question: str, config: dict):
    """
    get response output from model given params
    """
    cfg.logger.info("sending message")
    with llama_model_log():
        output = llm_backend.create_chat_completion(
            messages=[{
                "role": config.get('role'),
                "content": question,
                "top_p": config.get('top_p'),
                "temperature": config.get('temp'),
                "echo": False
            }]
        )
    cfg.logger.info("succesfully processed message")
    return output

@contextmanager
def llama_model_log(file_path="./llama.log"):
    """
    redirect output of llama.cpp model to a log called model.log
    """
    log_file = open(file_path, 'w')                   

    original_stdout = sys.stdout
    original_stderr = sys.stderr

    try:
        sys.stdout = log_file
        sys.stderr = log_file
        yield
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        log_file.close()
