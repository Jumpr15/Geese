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
     
     def insert_documents(self, documents):
          if isinstance(documents, list) is False:
               documents = [documents]
          try:
               self.client.upsert(
                    collection_name=self.collection_name,
                    points=[
                         models.PointStruct(
                              id=uuid4(),
                              payload=document,
                              vector=models.Document(text=document["content"], model=self.model_name),
                         )
                    for document in documents] 
               )
          except Exception as e:
               print(e)

     