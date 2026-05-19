import model as mdl
import config as cfg
import sys

def main() -> None:

    config_dict = cfg.read_config("./config.json")
    llm = mdl.init_model(config_dict)

    # basic loop for questioning model
    while True:
        q = input("\nEnter text or press Enter to quit: ")

        if not q:
            sys.exit(0)        
            
        output = mdl.llm_response(llm, q, config_dict)

        print(output['choices'][0]['message']['content'])


if __name__ == '__main__':
    main()
