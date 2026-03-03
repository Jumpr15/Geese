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
     },
     {
          "role": "user",
          "content": "can you perform a tool call using the specified tool calling format, use any args you want"
     }
]

available_tools_list = {
     get_weather.__name__: get_weather
}

res = client.chat.completions.create(
     model="deepseek.v3-v1:0",
     messages=messages,
     stream=False
)

res_text = res.choices[0].message.content
# print(res_text)

def execute_tool_call(tool_call):
     tool_name = tool_call["tool_name"]
     parameters = tool_call["parameters"]
     
     if tool_name in available_tools_list:
          tool = available_tools_list[tool_name]
          tool_result = tool(parameters)
          return tool_result
     
     return None
     
def check_tool_call(text):
     re_pattern = r"<Tool_Call>(.*?)</Tool_Call>"
     re_match = re.match(re_pattern, text, re.DOTALL)
     if re_match is None:
          return 
     
     tool_call = json.loads(re_match.group(1).strip())
     return execute_tool_call(tool_call)

print(res_text)
print(check_tool_call(res_text))