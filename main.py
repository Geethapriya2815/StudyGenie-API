# studygenie_api/main.py
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import List
import random

app = FastAPI(title="StudyGenie API")

# -----------------------------
# Models
# -----------------------------

class Student(BaseModel):
    id: int
    name: str
    course: str

class Doubt(BaseModel):
    question: str

class Note(BaseModel):
    content: str

class StudyPlanInput(BaseModel):
    hours_available: int
    topics: List[str]

# -----------------------------
# In-memory data storage
# -----------------------------
students = []
progress_logs = {}

# -----------------------------
# Sample AI responses (simulate Gemini)
# -----------------------------

def ai_answer_simulator(question: str) -> str:
    return f"(Simulated Gemini Answer) Here's a brief explanation for: '{question}'"

def summarize_simulator(text: str) -> str:
    return f"(Simulated Summary) Summary: {text[:50]}..."

def generate_study_plan(hours: int, topics: List[str]) -> List[str]:
    time_per_topic = hours // max(1, len(topics))
    return [f"Study '{topic}' for {time_per_topic} hour(s)." for topic in topics]

# -----------------------------
# Routes
# -----------------------------

@app.post("/students")
def register_student(student: Student):
    students.append(student)
    progress_logs[student.id] = []
    return {"message": "Student registered successfully!"}

@app.post("/ask")
def ask_doubt(doubt: Doubt):
    answer = ai_answer_simulator(doubt.question)
    return {"question": doubt.question, "answer": answer}

@app.post("/summarize")
def summarize_notes(note: Note):
    summary = summarize_simulator(note.content)
    return {"summary": summary}

@app.post("/study-plan")
def create_study_plan(plan_input: StudyPlanInput):
    plan = generate_study_plan(plan_input.hours_available, plan_input.topics)
    return {"plan": plan}

@app.get("/progress/{student_id}")
def get_progress(student_id: int):
    if student_id not in progress_logs:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"progress": progress_logs[student_id]}

@app.post("/progress/{student_id}/log")
def log_progress(student_id: int, task: str = Body(...)):
    if student_id not in progress_logs:
        raise HTTPException(status_code=404, detail="Student not found")
    progress_logs[student_id].append(task)
    return {"message": "Progress logged successfully!"}
