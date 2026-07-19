import chromadb
from sentence_transformers import SentenceTransformer

# ----------------------------
# Load Embedding Model
# ----------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")

# ----------------------------
# Connect to ChromaDB
# ----------------------------

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="sports_collection"
)

# ----------------------------
# Load Sports Data
# ----------------------------

def load_data():

    with open("data/sports.txt", "r", encoding="utf-8") as file:
        documents = file.readlines()

    # Remove previous data
    try:
        collection.delete(ids=[str(i) for i in range(1000)])
    except:
        pass

    for i, doc in enumerate(documents):

        embedding = model.encode(doc).tolist()

        collection.add(
            ids=[str(i)],
            documents=[doc],
            embeddings=[embedding]
        )

    print("✅ Sports data loaded into ChromaDB!")

# ----------------------------
# Search ChromaDB
# ----------------------------

def search_data(query, n_results=3):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "distances"]
    )

    documents = results["documents"][0]
    distances = results["distances"][0]

    context = "\n".join(documents)

    return context, distances