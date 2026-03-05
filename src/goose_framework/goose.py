import os
from dotenv import load_dotenv

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

goose = Goose(
     "deepseek.v3-v1:0",
     "You are a helpful ai assistant",
     tool_list
)

out = goose.fly(
     "perform a web search to retrive the latest daily news"
)

print(out)