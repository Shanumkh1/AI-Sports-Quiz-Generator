from src.quiz_generator import generate_quiz

context = """
Cricket is played between two teams of eleven players.
The ICC Cricket World Cup is one of the biggest cricket tournaments.
"""

quiz = generate_quiz(
    context=context,
    sport="Cricket",
    difficulty="Easy",
    num_questions=2
)

print(type(quiz))
print()

for q in quiz:
    print(q)
    print()