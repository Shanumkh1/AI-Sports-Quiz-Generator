from src.vector_store import search_data
from src.quiz_generator import generate_quiz

context = "\n".join(search_data("Cricket"))

quiz = generate_quiz(
    context=context,
    sport="Cricket",
    difficulty="Easy",
    num_questions=3
)

print(quiz)