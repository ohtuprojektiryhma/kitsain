from flask import Flask
from openai import OpenAI
from services.openai_service import OpenAIService
from config import OPENAI_API_KEY

app = Flask(__name__)

openai_service = OpenAIService(OpenAI(api_key=OPENAI_API_KEY))

import routes  # pylint: disable=W0611,C0413
