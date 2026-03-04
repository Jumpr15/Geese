def create_file(file_name: str, file_extension: str):
     res = {
          "file_name": f"{file_name}.{file_extension}",
          "file_created_at": "2/4/6",
          "response_status": "SUCCESS"
     }
     return str(res)

# no support for parameters currently
def agent_code_exec(func_name: str, func_params: dict):
     try:
          with open(func_name) as func:
               exec(func.read())
     except Exception as e:
          print(e)
     # currently no return value
     
"""
Create Python File -> in current directory only
{
     "tool_name": create_file,
     "parameters": {
          "file_name": str
          "file_extension": str
     }
}

Agent Code Execution -> in current directory only
{
     "tool_name": agent_code_exec,
     "parameters" : {
          func_name: str,
          func_params: {
               args...
          }
     }
}
"""