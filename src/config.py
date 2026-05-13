import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger.info('Started')

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
