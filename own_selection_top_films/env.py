from os import getenv
from dotenv import load_dotenv

load_dotenv()


def get_env(key: str) -> str:
    value = getenv(key)
    if value is None:
        raise EnvironmentError(f'The key with name {key} was not found in the env')
    return value
