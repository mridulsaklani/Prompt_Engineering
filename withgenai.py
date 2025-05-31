from http import client
import os
from urllib import response
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

genkey = os.getenv('GENAI_API_KEY')
project_id = os.getenv('PROJECT_ID')


client = genai.Client(api_key=genkey)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='who is mridul singh saklani'
)

print(response.text)