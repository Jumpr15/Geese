from datetime import datetime

def create_file(file_name: str, file_extension: str):
     curr_datetime = datetime.now()
     formatted_datetime = curr_datetime.strftime("%Y-%m-%s %H-%M-%S")
     
     res_status_flag = "SUCCESS"
     
     try:
          with open(f"{file_name}.{file_extension}", "w") as file:
               pass
     except Exception as e:
          res_status_flag = "FAILURE"
          print(e)
     
     res = {
          "file_name": f"{file_name}.{file_extension}",
          "file_created_at": formatted_datetime,
          "response_status": res_status_flag
     }
     return str(res)

# no support for parameters currently
def agent_code_exec(func_name: str):
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