import inspect

arr = []

def inspector_decorator(func):
     def inspector_wrapper(*args, **kwargs):
          func(*args, **kwargs)
          
          params = []
          sig = inspect.signature(func)
          args = sig.parameters.values()
          for arg in args:
               params.append(arg.name)
               
          arr.append({
               func.__name__: params
          })
          
     return inspector_wrapper

@inspector_decorator
def test_func(a, b):
     print(a + b)
     c = "string"
     return c
     
test_func(2, 2)
print(arr)