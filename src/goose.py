from model.model_class import Goose
from model.tools import sub_func, test_func, weather_func, is_currently_snowing

from builtin_tools.code_exec.exec import create_file, agent_code_exec

weather_func.recall = True
create_file.recall = True
tool_list = [weather_func, is_currently_snowing, create_file]

goose = Goose(
     "deepseek.v3-v1:0",
     "You are a helpful ai assistant",
     tool_list
)

out = goose.fly(
     "make a new python file called cow"
)

print(out)