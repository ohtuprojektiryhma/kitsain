import os
from flask import Flask
from openai import OpenAI
from dotenv import load_dotenv
from services.openai_service import OpenAIService


app = Flask(__name__)


dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass


openai_service = OpenAIService(OpenAI(api_key=os.getenv("OPENAI_API_KEY")))

import routes  # pylint: disable=W0611,C0413
