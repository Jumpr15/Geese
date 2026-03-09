import inspect
from datetime import datetime

def create_file_tool(file_name: str, file_extension: str):
     curr_datetime = datetime.now()
     formatted_datetime = curr_datetime.strftime("%Y-%m-%s %H-%M-%S")
     
     res_status_flag = "SUCCESS"
     
     try:
          with open(f"{file_name}.{file_extension}", "w") as file:
               pass
     except Exception as e:
          res_status_flag = "FAILURE"
          print(e)
     
     file_res = {
          "file_name": f"{file_name}.{file_extension}",
          "file_created_at": formatted_datetime,
          "response_status": res_status_flag
     }
     
     tool_name = inspect.currentframe().f_code.co_name
     
     arg_list = []
     sig = inspect.signature(create_file_tool) ### Manually set
     args = sig.parameters.values()
     for arg in args:
          arg_list.append(
               arg.name
          )
          
     res = {
          "tool_name": tool_name,
          "parameters": arg_list,
          "file_res": file_res
     }
     
     return str(res)

def write_to_file_tool(file_name: str, text_to_write: str):
     res_status_flag = True
     
     try:
          with open(file_name, "w") as file:
               file.write(text_to_write)
     except Exception as e:
          res_status_flag = False
          print(e)
         
     file_res = {
          "func_write_success": res_status_flag,
          "func_text_written": text_to_write  
     } 
     
     tool_name = inspect.currentframe().f_code.co_name
     
     arg_list = []
     sig = inspect.signature(write_to_file_tool) ### Manually set
     args = sig.parameters.values()
     for arg in args:
          arg_list.append(
               arg.name
          )
     
     res = {
          "tool_name": tool_name,
          "parameters": arg_list,
          "file_res": file_res    
     }
     
     return res

# no support for parameters currently
def execute_python_file_tool(func_name: str):
     res_status_flag = True
     
     try:
          with open(func_name) as func:
               print(exec(func.read()))
     except Exception as e:
          res_status_flag = False
          print(e)
          
     file_res = {
          "func_execution_success": res_status_flag,
          "func_return_value": None # no return value
     }
     
     return res
     
     tool_name = inspect.currentframe().f_code.co_name
     
     arg_list = []
     sig = inspect.signature(execute_python_file_tool) ### Manually set
     args = sig.parameters.values()
     for arg in args:
          arg_list.append(
               arg.name
          )
          
     res = {
          "tool_name": tool_name,
          "parameters": arg_list,
          "file_res": file_res         
     }
     
     return res
     
"""
Create Python File -> in current directory only
{
     "tool_name": create_file,
     "parameters": {
          "file_name": str
          "file_extension": str
     }
}

Agent Text/Code writing
{
     "tool_name": "write_to_file_tool",
     "parameters:: {
          file_name: str,
          text_to_write: str
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