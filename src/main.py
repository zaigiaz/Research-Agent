from llama_cpp import Llama
import json
import sys

# TODO :: Get Basic Text and Response Format in easy chat format kind of way
# TODO :: Create JSON config file
# TODO :: Arg-parsing for prompt and each kind of search backend
# TODO :: Follow Tutorial for tool-calling etc. (pydantic)

# Init basic Llama model
def init_model() -> Llama:
    # Basic pattern to initialize a model
    llm = Llama(
        model_path="/home/zaigiaz/third_party/ai_models/Qwen/Qwen3.5-9B-Q6_K.gguf",
        n_ctx=9056,
        verbose=False,
    )
    return llm

# Basic Output Object
def llm_response(llm_backend, question):
    output = llm_backend.create_chat_completion(
        messages=[{
         "role": "user",
         "content": question,
         "top_p": 0.9,
         "temperature": 0.5,
         "echo": False
        }]
    )
    return output

# parse command line inputs
def arg_parsing() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", type=str, required=True)
    parser.add_argument("-j", "--json", type=str, required=False)
    parser.add_argument("-c", "--ctx", type=int, required=False)
    parser.add_argument("--max-tokens", type=int, required=False)

    return vars(parser.parse_args())

# main function
def main():
    llm = init_model()

    # basic loop for questioning model
    while True:
        question = input("\nEnter text or press Enter to quit: ")

        if not question:
            sys.exit(0)        

        output = llm_response(llm, question)
        print(output['choices'][0]['message']['content'])

if __name__ == '__main__':
    main()
