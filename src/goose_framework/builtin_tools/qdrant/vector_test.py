import os
from dotenv import load_dotenv

from vector_store import Qdrant_Client

load_dotenv()

collection_name = "rag_collection"

qdrant = Qdrant_Client(
     os.getenv("QDRANT_CLUSTER_ENDPOINT"),
     os.getenv("QDRANT_CLUSTER_API_KEY"),
     collection_name
)

docs = [
     {"content": "The users pets name is Frederic the brawler"}, 
     {"content": "The users favourite food is french fries and golden curry"},
     {"content": "The user's favorite color is deep blue"},
     {"content": "The user works as a software engineer"},
     {"content": "The user lives in San Francisco, California"},
     {"content": "The user's hobbies include gaming, reading sci-fi novels, and hiking"},
     {"content": "The user prefers coffee over tea"},
     {"content": "The user's favorite movie genre is action and thriller"},
     {"content": "The user has been programming for 8 years"},
     {"content": "The user's favorite music artist is The Weeknd"},
     {"content": "The user speaks English and Spanish fluently"},
     {"content": "The user's birthday is March 15th"},
     {"content": "The user exercises 4 times a week at the gym"},
     {"content": "The user's favorite book is 'Dune' by Frank Herbert"},
     {"content": "The user prefers remote work environments"},
     {"content": "The user owns a 2020 Tesla Model 3"},
     {"content": "The user is allergic to shellfish"},
     {"content": "The user's favorite travel destination is Japan"},
]

qdrant.insert_documents(docs)
n = qdrant.document_ss_by_id({
     "content": "what is the users car"
})

for m in n:
     print(m)