### EXAMPLE USAGE OF LIBRARY 
### RAG WITH TOOL CALLING

import os
from dotenv import load_dotenv

from openai import OpenAI, AzureOpenAI

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
     return qdrant.document_ss_by_id_tool(query)

tool_list = [create_file_tool, write_to_file_tool, execute_python_file_tool, user_personal_information_query_vector_store, web_search_tool]

# client = OpenAI(
#   base_url=os.getenv("AZURE_KIMI_DEPLOYMENT_ENDPOINT"),
#   api_key=os.getenv("AZURE_FOUNDRY_API_KEY"),
# )

client = AzureOpenAI(
     base_url=os.getenv("AZURE_DEEPSEEK_DEPLOYMENT_ENDPOINT"),
     api_key=os.getenv("AZURE_FOUNDRY_API_KEY"),
     api_version="2024-12-01-preview"
)



goose = Goose(
     client,
     "DeepSeek-V3.2",
     "You are a helpful ai assistant",
     tool_list,
     ["violence", "hatred"]
)

while True:
     user_input = input("User prompt: ")

     out = goose.fly(
          user_input
     )

     print(out)
     for msg in goose.messages:
          print(msg)
