import os
from dotenv import load_dotenv

from openai import OpenAI

from model.model_class import Goose
from builtin_tools.brave_search.engine import web_search_tool
from builtin_tools.code_exec.exec import create_file_tool, write_to_file_tool, execute_python_file_tool
from builtin_tools.qdrant.vector_store import Qdrant_Client

load_dotenv()

qdrant = Qdrant_Client(
     os.getenv("QDRANT_CLUSTER_ENDPOINT"),
     os.getenv("QDRANT_CLUSTER_API_KEY"),
     "rag_collection"
)

def user_personal_information_query_vector_store(query):
     return qdrant.document_ss_by_id(query)

tool_list = [create_file_tool, write_to_file_tool, execute_python_file_tool, user_personal_information_query_vector_store, web_search_tool]

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPEN_ROUTER_API_KEY"),
)

goose = Goose(
     client,
     "qwen/qwen3-next-80b-a3b-instruct:free",
     "You are a helpful ai assistant",
     tool_list,
     ["violence", "hatred"]
)

out = goose.fly(
     "return a statement containing the words violence and hatred in exact name"
)

# openai/gpt-oss-120b:free
# qwen/qwen3-coder:free
# qwen/qwen3-next-80b-a3b-instruct:free

print(out)