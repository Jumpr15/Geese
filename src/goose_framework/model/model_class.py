import inspect
import json
import re

from model.prompt_template import build_prompt_template

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
                    "tool_func": tool,
                    "tool_block": hasattr(tool, "recall")
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
                    tool_output = tool["tool_func"](**parameters)
                    return tool_output
               
          return None
     
     def check_tool_call(self, text):
          re_pattern = r"<Tool_Call>(.*?)</Tool_Call>"
          re_match = re.findall(re_pattern, text, re.DOTALL)
          
          if not re_match:
               return None
          
          recall_flag = False
          out = []
          for match in re_match:
               if re_match is None:
                    pass
               
               tool_call = json.loads(match)
               tool_output = self.execute_tool_call(tool_call)
               
               recall_flag = True
               
               out.append(tool_output)
               
          return [ out, recall_flag ]
     
     def fly(self, prompt):
          while True:
               messages_copy = self.messages.copy()
               messages_copy.append({
                    "role": "user",
                    "content": prompt
               })
               
               res = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages_copy,
                    stream=False      
               )
               
               res_text = res.choices[0].message.content
               tool_result = self.check_tool_call(res_text)
               if tool_result is None:
                    break

               tool_output, recall_bool = tool_result
               
               if recall_bool == False:
                    break
               
               prompt = prompt + f"Tool Response Context Section: {str(tool_output)}. Answer users original prompt."

          messages_copy.append({
               "role": "user",
               "content": prompt
          })
          return res_text
          