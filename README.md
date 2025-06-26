# 📚 StudyGenie API

A RESTful API built with **FastAPI** that simulates a Gemini-style AI study assistant for students. It allows students to register, ask academic questions, summarize notes, create study plans, and track their progress.

----

## 🚀 Features!

* 📌 Register student profiles
* 🤖 Ask academic questions and get simulated AI answers
* 📝 Summarize long study notes
* 📆 Generate personalized study plans
* 📈 Log and view student progress

---

## 🛠 Tech Stack

* **Python 3.9+**
* **FastAPI** - Web framework for building APIs
* **Uvicorn** - ASGI server to run the app

---

## 🔧 Installation

1. Clone the repository:

```bash
https://github.com/yourusername/studygenie-api.git
```

2. Navigate into the project folder:

```bash
cd studygenie-api
```

3. Install dependencies:

```bash
pip install fastapi uvicorn
```

4. Run the server:

```bash
uvicorn main:app --reload
```

5. Open in browser:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📬 API Endpoints

### 1. Register Student

**POST** `/students`

```json
{
  "id": 1,
  "name": "Geethapriya",
  "course": "AI & Data Science"
}
```

### 2. Ask Doubt

**POST** `/ask`

```json
{
  "question": "What is machine learning?"
}
```

### 3. Summarize Notes

**POST** `/summarize`

```json
{
  "content": "Machine learning is the process of..."
}
```

### 4. Create Study Plan

**POST** `/study-plan`

```json
{
  "hours_available": 3,
  "topics": ["Python", "ML", "SQL"]
}
```

### 5. Log Student Progress

**POST** `/progress/{student_id}/log`

```text
"Completed Python basics"
```

### 6. View Student Progress

**GET** `/progress/{student_id}`

---

## 📦 Future Enhancements

* ✅ Integrate with real AI (Gemini or OpenAI)
* ✅ Store data using SQLite or MongoDB
* ✅ Add JWT authentication
* ✅ Build frontend using React or HTML

---

## 🧑 Author

Made with ❤️ by **Geethapriya S.L.**

---

## 📜 License

This project is licensed under the MIT License.
