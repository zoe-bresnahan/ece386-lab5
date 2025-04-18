"""Passes a personal intro statement to an LLM.
The LLM produces valid JSON that could be ingested into a database to create a new user.

Modified from https://ollama.com/blog/structured-outputs
"""

from ollama import chat
from pydantic import BaseModel
import sys


class User(BaseModel):
    name: str
    age: int
    color: str | None
    favorite_toy: str | None
    favorite_activity: str | None


prompt = sys.argv[1]  # first argument after user_creation.py


response = chat(  # from terminal to the LLM "prompt" variable
    messages=[
        {
            "role": "user",
            "content": prompt,
        },
        {
            "role": "system",
            "content": """
        Return your answer in JSON.
      """,
        },
    ],
    model="gemma:2b",
    format=User.model_json_schema(),
)

pets = User.model_validate_json(response.message.content)
print(pets)
