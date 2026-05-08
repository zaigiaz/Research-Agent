from llama_cpp import Llama

# TODO :: Get Basic Text and Response Format in easy chat format kind of way
# TODO :: Create JSON config file
# TODO :: Arg-parsing for prompt and each kind of search backend
# TODO :: Follow Tutorial for tool-calling etc. (pydantic)

# Init basic Llama model
def init_model() -> Llama:
    # Basic pattern to initialize a model
    llm = Llama(
        model_path="/home/zaigiaz/third_party/ai_models/Qwen/Qwen3.5-9B-Q6_K.gguf",
        # n_gpu_layers=-1, 
        # seed=1337, 
        n_ctx=9056,
    )
    return llm

# parse command line inputs
def arg_parsing() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--ctx", type=int, required=False)
    parser.add_argument("--max-tokens", type=int, required=False)

    return vars(parser.parse_args())


def main():
    llm = init_model()

    # Basic Output Object
    output = llm(
        "Question: Name the planets in the solar system?",
        max_tokens=24,
        echo=False 
    )
    print(output['choices'][0]["text"])


if __name__ == '__main__':
    main()
