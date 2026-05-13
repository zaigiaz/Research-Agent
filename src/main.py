import model as mdl
import config as cfg

def main() -> None:

    # argparse_dict = 
    config_dict = cfg.read_config("./config.json")
    llm = mdl.init_model(config_dict)

    # basic loop for questioning model
    while True:
        question = input("\nEnter text or press Enter to quit: ")

        if not question:
            sys.exit(0)        

        # temp test message
        q = "you are local agent who can do bash commmands, by calling {tool-call: '<bash_command>'}, be concise and show the current directory and files with tool call"
        output = mdl.llm_response(llm, q, config_dict)

        print(output['choices'][0]['message']['content'])


if __name__ == '__main__':
    main()
