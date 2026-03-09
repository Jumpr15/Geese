from typing import Union

import inspect
from uuid import uuid4
from qdrant_client import QdrantClient, models
from fastembed import TextEmbedding

class Qdrant_Client:
     def __init__(self, url: str, api_key: str, collection_name: str):
          try:
               self.client = QdrantClient(
                    url=url, 
                    api_key=api_key
               )
               self.collection_name = collection_name
               self.model_name = "BAAI/bge-small-en" ###
               self.vector_dims = 384 ###   
               
               
               if self.client.collection_exists(collection_name) is False:
                    self.client.create_collection(
                         collection_name=collection_name,
                         vectors_config=models.VectorParams(size=self.vector_dims, distance=models.Distance.COSINE)
                    )                    
                          
               
          except Exception as e:
               print(e)
               
               
     def vector_embed(self, text):
          embedding_generator = self.embedder.embed(text)
          embedding_list = list(embedding_generator)
          return embedding_list[0]
     
     def insert_documents_tool(self, documents: Union[list, dict]):
          if isinstance(documents, list) is False:
               documents = [documents]
          
          insert_res = self.client.upsert(
               collection_name=self.collection_name,
               points=[
                    models.PointStruct(
                         id=uuid4(),
                         payload=document,
                         vector=models.Document(text=document["content"], model=self.model_name),
                    )
               for document in documents] 
          )
          
          tool_name = inspect.currentframe().f_code.co_name
          
          arg_list = []
          sig = inspect.signature(self.insert_documents_tool) ### Manually set
          args = sig.parameters.values()
          for arg in args:
               arg_list.append(
                    arg.name
               )
               
          res = {
               "tool_name": tool_name,
               "parameters": arg_list,
               "insert_result": insert_res  
          }


     def document_ss_by_id_tool(self, query_text): 
          # returns nearest points 
          query_vectors = self.client.query_points(
               collection_name=self.collection_name,
               query=models.Document(text=query_text, model=self.model_name),
               limit=2
          )
          
          formatted_queries = []
          for vector in query_vectors.points:
               formatted_queries.append({
                    "id": vector.id,
                    "score": vector.score,
                    "payload": vector.payload
               })
               
          tool_name = inspect.currentframe().f_code.co_name
     
          arg_list = []
          sig = inspect.signature(self.document_ss_by_id_tool) ### Manually set
          args = sig.parameters.values()
          for arg in args:
               arg_list.append(
                    arg.name
               )
               
               res = {
                    "tool_name": tool_name,
                    "parameters": arg_list,
                    "query_result": formatted_queries
               }
               
          return formatted_queries