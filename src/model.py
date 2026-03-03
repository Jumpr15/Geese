from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

system_prompt = """

You are helpful AI assistant.

Tool Calls Available:
{
    "name": "get_weather",
    "parameters": {
        "city": "string(required)",
        "parameter2": "string(required_value: c/f)"
    }
}

"""

messages = [
     {
          "role": "system",
          "content": system_prompt
     },
     {
          "role": "user",
          "content": "what token do you use to indicate a tool call"
     },
     {
          "role": "user",
          "content": "how would i detect this token and isolate the insides"
     }
]

res = client.chat.completions.create(
     model="deepseek.v3-v1:0",
     messages=messages
)

res_text = res.choices[0].message.content
print(res_text)

