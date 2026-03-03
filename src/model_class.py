import inspect

class Goose():
     def __init__(
          self, 
          model,
          system_prompt: str,
          tool_list: list
     ):
          self.available_tool_list = []
          for tool in tool_list:
               params = []
               sig = inspect.signature(tool)
               args = sig.parameters.values()
               for arg in args:
                    params.append(
                         arg.name
                    )
                    
               self.available_tool_list.append(f"""
                    "tool_name": {tool.__name__},
                    "parameter_list": {params}
               """)
               
               system_message = system_prompt + """\n
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

Tool Calls Available:\n
""" + '\n'.join(self.available_tool_list)
          
          self.messages = [
               {
                    "role": "system",
                    "content": system_message
               }
          ]
 
if __name__ == "__main__":
     def sub_func(a, b):
          print(a - b)
          
     def test_func(a, b):
          print(a + b)
          c = "string"

     tool_list = [sub_func, test_func]
     goose = Goose("d", "You are a helpful ai assistant", tool_list)
     print(goose.messages[0]["content"])