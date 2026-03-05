import os
from dotenv import load_dotenv

from vector_store import Qdrant_Client

load_dotenv()

collection_name = "test_collection"

qdrant = Qdrant_Client(
     os.getenv("QDRANT_CLUSTER_ENDPOINT"),
     os.getenv("QDRANT_CLUSTER_API_KEY"),
     collection_name
)

docs = [
     {"content": "document1"}, 
     {"content": "document2"}
]

qdrant.insert_documents(docs)