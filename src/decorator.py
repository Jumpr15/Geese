import inspect

tool_list = [] # MUST RUN FUNC FINISH TO REGISTER

def inspector_decorator(func):
     def inspector_wrapper(*args, **kwargs):
          func(*args, **kwargs)
          
          params = []
          sig = inspect.signature(func)
          args = sig.parameters.values()
          for arg in args:
               params.append(
                    arg.name
               )
               
          tool_list.append({ ### MANUAL SET
               "tool_name": func.__name__,
               "parameter_list": params
          })
          
     return inspector_wrapper

def format_tool_list(tool_list: list) -> list:
     for tool in tool_list:
          formatted_tool = f"""
          tool_name: {tool['tool_name']}
          params: {tool['parameter_list']}
          """

@inspector_decorator
def test_func(a, b):
     print(a + b)
     c = "string"
     return c

@inspector_decorator
def sub_func(a, b):
     print(a - b)

     
test_func(2, 2)
sub_func(5, 2)
print(tool_list)
