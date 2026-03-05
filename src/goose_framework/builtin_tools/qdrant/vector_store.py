from qdrant_client import QdrantClient, models
from fastembed import TextEmbed

class Qdrant_Client:
     def __init__(self, url: str, api_key: str, collection_name: str):
          try:
               client = QdrantClient(
                    url, 
                    api_key
               )
               self.client = client
          except Exception as e:
               print(e)
               
          if client.collection_exists(
               collection_name=collection_name
          ):
               self.collection_name = collection_name
          else:
               client.create_collection(
                    collection_name=collection_name,
                    vectors_config=models.VectorParams(size=25, distance=models.Distance.COSINE)
               )
               
          self.embedder = TextEmbed('BAAI/bge-small-en-v1.5')
               
     def vector_embed(self, text_list):
          