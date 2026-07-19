import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def search_web(query):

    print("Searching Tavily...")

    response = client.search(
        query=f"{query} sport facts",
        max_results=5
    )

    print(response)

    context = ""

    for result in response.get("results", []):
        context += result.get("content", "") + "\n\n"

    return context