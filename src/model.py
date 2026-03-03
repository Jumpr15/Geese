import re

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

system_prompt = """

You are helpful AI assistant.

Calling Tools Procedure:

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
          "content": "can you perform a tool call using the specified tool calling format, use any args you want"
     }
]

res = client.chat.completions.create(
     model="deepseek.v3-v1:0",
     messages=messages,
     stream=False
)

res_text = res.choices[0].message.content
# print(res_text)

check_tool_call

regex_match = re.match(r"<Tool_Call>(.*?)</Tool_Call>", res_text, re.DOTALL)
print(regex_match.group(1).strip())