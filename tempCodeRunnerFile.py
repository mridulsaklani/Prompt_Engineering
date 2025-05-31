
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

key = os.getenv('OPENAI_API_KEY')


client = OpenAI()

bhdk = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "Talk like a pirate."},
        {
            "role": "user",
            "content": "How do I check if a Python object is an instance of a class?",
        },
    ],
)


print(bhdk.choices[0].message.content)