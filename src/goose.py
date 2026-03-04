from model.model_class import Goose
from model.tools import sub_func, test_func, weather_func, is_currently_snowing

from builtin_tools.code_exec.exec import create_file, agent_code_exec

weather_func.recall = True
create_file.recall = True
agent_code_exec.recall = True
tool_list = [weather_func, is_currently_snowing, create_file, agent_code_exec]

goose = Goose(
     "deepseek.v3-v1:0",
     "You are a helpful ai assistant",
     tool_list
)

out = goose.fly(
     "Can you execute the python file hello.py using agent_code_exec tool call"
)

print(out)