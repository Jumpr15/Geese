import os
from dotenv import load_dotenv

from model.model_class import Goose
from builtin_tools.code_exec.exec import create_file_tool, write_to_file_tool, execute_python_file_tool
from builtin_tools.qdrant.vector_store import Qdrant_Client

load_dotenv()

qdrant = Qdrant_Client(
     os.getenv("QDRANT_CLUSTER_ENDPOINT"),
     os.getenv("QDRANT_CLUSTER_API_KEY"),
     "rag_collection"
)

create_file_tool.recall = True
execute_python_file_tool.recall = True
write_to_file_tool.recall = True

tool_list = [create_file_tool, write_to_file_tool, execute_python_file_tool]

goose = Goose(
     "deepseek.v3-v1:0",
     "You are a helpful ai assistant",
     tool_list
)

out = goose.fly(
     "Create a new python file named anaconda.py and write in the file code to print 'i am a anaconda' and then execute it"
)

print(out)