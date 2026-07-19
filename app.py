import streamlit as st
from src.vector_store import search_data
from src.quiz_generator import generate_quiz
from src.web_search import search_web

# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="AI Sports Quiz Generator",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 AI Sports Quiz Generator")
st.write("Generate AI-powered sports quizzes using Retrieval-Augmented Generation (RAG).")

# ---------------------------------
# Sidebar
# ---------------------------------

st.sidebar.header("Quiz Settings")

sport = st.sidebar.selectbox(
    "Select Sport",
    [
        "Cricket",
        "Football",
        "Basketball",
        "Tennis",
        "Hockey",
        "Kabaddi"
    ]
)

difficulty = st.sidebar.selectbox(
    "Difficulty",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
)

num_questions = st.sidebar.slider(
    "Number of Questions",
    min_value=1,
    max_value=10,
    value=5
)

# ---------------------------------
# Generate Quiz
# ---------------------------------

if st.sidebar.button("Generate Quiz"):

    with st.spinner("Searching local database..."):

        context, count = search_data(sport)

    # If nothing useful is found locally, use Tavily
    if count == 0 or sport.lower() not in context.lower():

        st.warning("Local information not found.")
        st.info("Searching the web using Tavily...")

        context = search_web(sport)

    else:

        st.success("Information retrieved from ChromaDB.")

    try:

        with st.spinner("Generating quiz..."):

            quiz = generate_quiz(
                context=context,
                sport=sport,
                difficulty=difficulty,
                num_questions=num_questions
            )

        st.session_state.quiz = quiz

    except Exception as e:

        st.error(f"Quiz generation failed.\n\n{e}")

# ---------------------------------
# Display Quiz
# ---------------------------------

if "quiz" in st.session_state:

    st.header("📝 Quiz")

    answers = {}

    for i, question in enumerate(st.session_state.quiz):

        st.subheader(f"Question {i+1}")

        st.write(question["question"])

        answers[i] = st.radio(
            "Choose one:",
            options=list(question["options"].keys()),
            format_func=lambda x: f"{x}. {question['options'][x]}",
            key=f"question_{i}"
        )

        st.markdown("---")

    # ---------------------------------
    # Submit Quiz
    # ---------------------------------

    if st.button("Submit Quiz"):

        score = 0

        st.header("🏆 Results")

        for i, question in enumerate(st.session_state.quiz):

            selected = answers[i]
            correct = question["answer"]

            if selected == correct:

                score += 1

                st.success(f"Question {i+1}: Correct ✅")

            else:

                st.error(f"Question {i+1}: Incorrect ❌")

                st.write(
                    f"Correct Answer: **{correct}. {question['options'][correct]}**"
                )

            st.write("")

        total = len(st.session_state.quiz)

        percentage = (score / total) * 100

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Score", f"{score}/{total}")

        with col2:
            st.metric("Percentage", f"{percentage:.1f}%")

        st.progress(percentage / 100)

        if percentage == 100:

            st.balloons()
            st.success("🎉 Perfect Score!")

        elif percentage >= 80:

            st.success("🌟 Excellent!")

        elif percentage >= 60:

            st.info("👍 Good Job!")

        else:

            st.warning("📚 Keep Practicing!")

# ---------------------------------
# Reset Quiz
# ---------------------------------

if "quiz" in st.session_state:

    if st.button("Generate New Quiz"):

        del st.session_state.quiz
        st.rerun()

# ---------------------------------
# Footer
# ---------------------------------

st.markdown("---")
st.caption(
    "Built with ❤️ using Streamlit, ChromaDB, SentenceTransformers, OpenRouter, and Tavily."
)