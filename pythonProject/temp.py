import os

from dotenv import load_dotenv
from openai import api_key

load_dotenv()

TOKEN = os.environ.get("TOKEN")
api_key_env = os.environ.get("api_key")

print(api_key_env)