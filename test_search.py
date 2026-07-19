from src.vector_store import search_data

results = search_data("Which sport uses a bat?")

print("\nSearch Results:\n")

for item in results:
    print("-", item)