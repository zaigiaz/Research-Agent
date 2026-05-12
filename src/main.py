from llama_cpp import Llama
from contextlib import contextmanager
import json
import os
import logging
import sys

# TODO :: create class wrapper around llama-cpp-python stuff
# TODO :: Follow Tutorial for tool-calling etc. (pydantic)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger.info('Started')

def init_model(config: dict) -> Llama:
    """
    Basic Model Init, read params from json config later
    """
    with llama_model_log():
        llm = Llama(
            model_path = config.get('model'),
            n_ctx      = config.get('n_ctx'),
            verbose    = True,
        )
    return llm

@contextmanager
# TODO :: have this log in the dedicated <Task> Folder and make sure we get full output instead of cutoff
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


def llm_response(llm_backend, question: str, config: dict):
    """
    get response output from model given params
    """
    logger.info("sending message")
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
    logger.info("succesfully processed message")
    return output


def read_config(file_path: str) -> dict:
    """
    read json config file in project dir and return values specified as dict
    if not specified then it will be None
    """
    try:
        with open(file_path, mode='r') as json_file:
            data = json.load(json_file)

            config = {
                'model': data.get('model', None),
                'role': data.get('role', None),
                'n_ctx': data.get('n_ctx', None),
                'top_p': data.get('top_p', None),
                'max-tokens': data.get('max-tokens', None),
	        'report_type': data.get('report_type', None),
            }

            logger.info("config file read")
            return config

    except FileNotFoundError:
        print("File not found!")
    except JSONDecodeError:
        print("Invalid JSON format!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    
def arg_parsing() -> dict:
    """
    command line parsing for local model params and search backends
    """
    parser = argparse.ArgumentParser()

    # model params
    parser.add_argument("-m", "--model", type=str, required=True)
    parser.add_argument("-j", "--json", type=str, required=False)
    parser.add_argument("-c", "--ctx", type=int, required=False)
    parser.add_argument("--max-tokens", type=int, required=False)

    # search backends
    parser.add_argument("-d", "--duckduckgo", type=bool, required=False)
    parser.add_argument("-a", "--arxiv", type=bool, required=False)
    
    return vars(parser.parse_args())

    
def main():

    config_dict = read_config("./config.json")
    llm = init_model(config_dict)

    # basic loop for questioning model
    while True:
        question = input("\nEnter text or press Enter to quit: ")

        if not question:
            sys.exit(0)        

        # temp test message
        q = "you are local agent who can do bash commmands, by calling {tool-call: '<bash_command>'}, be concise and show the current directory and files with tool call"
        output = llm_response(llm, q, config_dict)

        print(output['choices'][0]['message']['content'])

if __name__ == '__main__':
    main()
