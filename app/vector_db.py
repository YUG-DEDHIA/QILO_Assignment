# app/vector_db.py
import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text, chunk_size=200):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def store_chunks(chunks: list):
    embeddings = model.encode(chunks)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    faiss.write_index(index, "vector_db.index")
    with open("chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

def retrieve_top_chunks(query: str, top_k: int = 3) -> list:
    index = faiss.read_index("vector_db.index")
    with open("chunks.pkl", "rb") as f:
        stored_chunks = pickle.load(f)
    query_embedding = model.encode([query])
    _, I = index.search(query_embedding, top_k)
    return [stored_chunks[i] for i in I[0]]

# Example usage
if __name__ == "__main__":
    content = "Luke Skywalker is a fictional character and the main protagonist of the original trilogy of the Star Wars franchise."
    chunks = chunk_text(content)
    store_chunks(chunks)
    query = "Who is Luke Skywalker?"
    top_chunks = retrieve_top_chunks(query)
    print(top_chunks)
