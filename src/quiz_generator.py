import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


def generate_quiz(context, sport, difficulty, num_questions):

    prompt = f"""
You are a sports quiz generator.

Use ONLY the information below.

CONTEXT:
{context}

Generate exactly {num_questions} multiple-choice questions.

Sport: {sport}
Difficulty: {difficulty}

Return ONLY valid JSON.

The JSON format must be:

[
  {{
    "question": "...",
    "options": {{
      "A": "...",
      "B": "...",
      "C": "...",
      "D": "..."
    }},
    "answer": "A"
  }}
]

Do not write markdown.
Do not use ```json.
Do not write explanations.
Return only the JSON array.
"""

    response = client.chat.completions.create(
        model="tencent/hy3:free",
        messages=[
            {
                "role": "system",
                "content": "Return only valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=1000,
    )

    text = response.choices[0].message.content.strip()

    # Remove markdown if the model accidentally includes it
    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)