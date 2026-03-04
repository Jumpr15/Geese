import inspect
import json
import re

from prompt_template import build_prompt_template
from tools import sub_func, test_func

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

class Goose():
     def __init__(
          self, 
          model,
          system_prompt: str,
          input_tool_list: list
     ):
          self.client = OpenAI()
          self.model = model
          
          self.tool_list = []
          
          for tool in input_tool_list:
               params = []
               sig = inspect.signature(tool)
               args = sig.parameters.values()
               for arg in args:
                    params.append(
                         arg.name
                    )
               
               self.tool_list.append({
                    "tool_name": tool.__name__,
                    "parameter_list": params,
                    "tool_func": tool
               })
               
          self.messages = [
               {
                    "role": "system",
                    "content": build_prompt_template(system_prompt, self.tool_list)
               }
          ]
          
     def execute_tool_call(self, tool_call):
          tool_name = tool_call["tool_name"]
          parameters = tool_call["parameters"]
          
          for tool in self.tool_list:
               if tool_name == tool["tool_name"]:
                    tool_result = tool["tool_func"](**parameters)
                    return tool_result
               
          return None
     
     def check_tool_call(self, text):
          re_pattern = r"<Tool_Call>(.*?)</Tool_Call>"
          re_match = re.search(re_pattern, text, re.DOTALL)
          if re_match is None:
               return None
          
          tool_call = json.loads(re_match.group(1).strip())
          print(f"Tool Call is: {tool_call}")
          out = self.execute_tool_call(tool_call)
          return out
     
     def fly(self, prompt):
          while True:
               self.messages.append({
                    "role": "user",
                    "content": prompt
               })
               
               res = self.client.chat.completions.create(
                    model=self.model,
                    messages=self.messages,
                    stream=False      
               )
               
               res_text = res.choices[0].message.content
               tool_result = self.check_tool_call(res_text)

          return res_text, tool_result
          
if __name__ == "__main__":

     tool_list = [sub_func, test_func]
     goose = Goose("deepseek.v3-v1:0", "You are a helpful ai assistant", tool_list)
     output, tool_output = goose.fly("can you call test_func, a=6, b=4")
     print(output, tool_output)