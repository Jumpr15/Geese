import inspect
import subprocess

def shell_cmd_tool(cmd):
     process = subprocess.Popen(
          cmd,
          shell=True,
          text=True,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE
     )
     stdout, stderr = process.communicate()
     
     tool_name = inspect.currentframe().f_code.co_name
     arg_list = []
     sig = inspect.signature(shell_cmd_tool) ### Manually set
     args = sig.parameters.values()
     for arg in args:
          arg_list.append(
               arg.name
          )
     
     return {
          "tool_name": tool_name,
          "parameters": arg_list,
          "shell_return_values": {
               "stdout": stdout.strip(),
               "stderr": stderr.strip()
          }
     }

sj = shell_cmd_tool("ls")
print(sj)