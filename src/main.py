from llama_cpp import Llama

# TODO :: Get Basic Text and Response Format in easy chat format type of way
# TODO :: Create Toml or yaml object for config file
# TODO :: Follow Tutorial for tool-calling etc.

# Basic pattern to initialize a model
llm = Llama(
      model_path="/home/zaigiaz/third_party/ai_models/Qwen/Qwen3.5-9B-Q6_K.gguf",
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      n_ctx=9056, # Uncomment to increase the context window
)

# Basic Output Object
output = llm(
      "Q: Name the planets in the solar system? A: ", # Prompt
      max_tokens=256, # Generate up to 32 tokens, set to None to generate up to the end of the context window
      stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
      echo=True # Echo the prompt back in the output
) # Generate a completion, can also call create_completion

print(output)
