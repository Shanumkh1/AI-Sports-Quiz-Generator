# 🏆 AI Sports Quiz Generator

An AI-powered Sports Quiz Generator built using **Streamlit**, **ChromaDB**, **Sentence Transformers**, **OpenRouter**, and **Tavily**. The application uses **Retrieval-Augmented Generation (RAG)** to generate intelligent sports quizzes based on local knowledge and falls back to web search when required.

---

## 📌 Features

- 🏏 Generate quizzes for multiple sports
- 🎯 Select difficulty level (Easy, Medium, Hard)
- 🔢 Choose the number of quiz questions
- 🧠 AI-generated multiple-choice questions
- 📚 Retrieval-Augmented Generation (RAG)
- 💾 Local knowledge retrieval using ChromaDB
- 🌐 Web search fallback using Tavily
- 🤖 Quiz generation using OpenRouter LLM
- ✅ Automatic scoring
- 📊 Progress bar and performance feedback
- 🎉 Interactive Streamlit interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- OpenRouter API
- Tavily Search API
- LangChain Concepts (RAG)
- JSON
- Git & GitHub

---

## 📂 Project Structure

```text
AI-Sports-Quiz-Generator/
│
├── app.py
├── load_data.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── sports.txt
│
├── src/
│   ├── __init__.py
│   ├── vector_store.py
│   ├── quiz_generator.py
│   ├── web_search.py
│   ├── prompts.py
│   └── rag.py
│
├── prompts/
├── tests/
├── utils/
└── chroma_db/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shanumkh1/AI-Sports-Quiz-Generator.git
```

### 2. Navigate to the project

```bash
cd AI-Sports-Quiz-Generator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## 📥 Load the Vector Database

Run:

```bash
python load_data.py
```

This loads the sports knowledge into ChromaDB.

---

## ▶️ Run the Application

```bash
python -m streamlit run app.py
```

---

## 🚀 How It Works

1. User selects:
   - Sport
   - Difficulty
   - Number of Questions

2. ChromaDB searches the local sports knowledge base.

3. If relevant information is unavailable, Tavily searches the web.

4. The retrieved context is sent to the OpenRouter LLM.

5. The LLM generates multiple-choice quiz questions.

6. Users answer the questions.

7. The application evaluates the answers and displays:
   - Score
   - Percentage
   - Performance message

---

## 🧠 RAG Workflow

```text
User Input
      │
      ▼
ChromaDB Vector Search
      │
      ├──────────────► Relevant Data Found
      │                      │
      │                      ▼
      │              OpenRouter LLM
      │
      ▼
No Relevant Data
      │
      ▼
Tavily Web Search
      │
      ▼
OpenRouter LLM
      │
      ▼
Generated Quiz
      │
      ▼
User Answers
      │
      ▼
Score & Feedback
```

---

## 📸 Screenshots

Add screenshots here after running the application.

Example:

- Home Screen
- Quiz Generation
- Quiz Results

---

## 🔮 Future Enhancements

- User authentication
- Leaderboard
- Timer-based quizzes
- More sports categories
- Quiz history
- PDF score report
- Voice-enabled quiz
- Multiplayer mode

---

## 👨‍💻 Author

**Shanumkh**

GitHub:  
https://github.com/Shanumkh1

---

## 📜 License

This project is developed for educational and learning purposes.
