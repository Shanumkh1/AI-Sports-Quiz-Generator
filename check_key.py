import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

if key:
    print("Key found!")
    print("Starts with:", key[:10])
    print("Length:", len(key))
else:
    print("No key found!")