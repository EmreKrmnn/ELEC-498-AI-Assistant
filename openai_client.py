from openai import OpenAI
from API_Key_Config import get_openai_api_key

client = OpenAI(api_key=get_openai_api_key())
