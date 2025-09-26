from dotenv import load_dotenv
from pathlib import Path
import os


def get_token_from_env_variable():
    env_path = Path(__file__).resolve().parent.parent / '.env'
    load_dotenv(env_path)
    return os.getenv('TOKEN')

