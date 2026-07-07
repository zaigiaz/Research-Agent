import model as mdl
import config as cfg
import sys
import tools as tl

def main() -> None:

    config_dict = cfg.read_config("./actual_config.json")
    llm = mdl.init_model(config_dict)

    # basic loop for questioning model
    while True:
        q = input("\nEnter text or press Enter to quit: ")

        if not q:
            sys.exit(0)        
            
        output = mdl.llm_response(llm, q, config_dict)
        msg = output['choices'][0]['message']['content']
        print(msg)

        t_list = tl.parse_review(msg)
        print("\nhere is the tools that were found: ", t_list, "\n")

        sys.exit(0)


if __name__ == '__main__':
    main()
