from llama_cpp import Llama
from contextlib import contextmanager
import json
import os
import logging
import sys

# TODO :: add function to read config file
# TODO :: Follow Tutorial for tool-calling etc. (pydantic)
# TODO :: create class wrapper around llama-python stuff

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger.info('Started')

def init_model():
    """
    Basic Model Init, read params from json config later
    """
    with llama_model_log():
        llm = Llama(
            model_path="/home/zaigiaz/third_party/ai_models/Qwen/Qwen3.5-9B-Q6_K.gguf",
            n_ctx=9056,
            verbose=True,
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


# TODO :: Get Basic Text and Response Format in easy chat format kind of way
def llm_response(llm_backend, question):
    """
    get response output from model given params
    """
    logger.info("sending message")
    with llama_model_log():
        output = llm_backend.create_chat_completion(
            messages=[{
                "role": "user",
                "content": question,
                "top_p": 0.9,
                "temperature": 0.5,
                "echo": False
            }]
        )
    logger.info("succesfully processed message")
    return output


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
    llm = init_model()

    # basic loop for questioning model
    while True:
        question = input("\nEnter text or press Enter to quit: ")

        if not question:
            sys.exit(0)        

        output = llm_response(llm, "give me a short sentence in old english, a greeting would be nice!")
        print(output['choices'][0]['message']['content'])

if __name__ == '__main__':
    main()
