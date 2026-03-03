import json
import re

from example_tools import get_weather

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

system_prompt = """

You are helpful AI assistant.

Calling Tools Procedure:
### IMPORTANT <Tool_Call> and </Tool_Call> must be called in this exact spelling and capitalisation

<Tool_Call>
{
     "tool_name": tool name to call,
     "parameters": {
          key pair values of parameter and parameter values for all parameters in parameter_list
     }
}
</Tool_Call>

Tool Calls Available:
{
    "name": "get_weather",
    "parameters": {
        "city": "string(required)",
        "temperature_format": "string(required_value: c/f)"
    }
}

"""

messages = [
     {
          "role": "system",
          "content": system_prompt
     }
]

# available_tools_list = {
#      get_weather.__name__: get_weather
# }

res = client.chat.completions.create(
     model="deepseek.v3-v1:0",
     messages=messages,
     stream=False
)

# res_text = res.choices[0].message.content
# print(res_text)

if __name__ == "__main__":
     while True:
          user_prompt = input("User Prompt: ")
          if user_prompt.lower() == "exit":
               break
          
          messages.append({
               "role": "user",
               "content": user_prompt
          })
          
          res = client.chat.completions.create(
               model="deepseek.v3-v1:0",
               messages=messages,
               stream=False
          )
          messages.append({
               "role": "assistant",
               "content": res.choices[0].message.content
               })
          
          for message in messages:
               print(f"{message["role"]}: {message["content"]}")
               print("-------------")     