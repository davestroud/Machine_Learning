import chromadb
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('sentence-transformers/msmarco-distilbert-dot-v5')

docs = ["Around 9 Million people live in London", "London is known for its financial district"]
query = "How many people live in London?"

query_emb = model.encode(query)
doc_emb = model.encode(docs)

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

collection.add(
    embeddings=doc_emb.tolist(),
    documents=docs,
    ids=["id1", "id2"])

collection.query(
    query_embeddings=query_emb.tolist(),
    n_results=1)