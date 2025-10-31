from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

students={
    1: {
        "name": "John",
        "age": 17,
        "year": "12th"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdatedStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

app=FastAPI()

@app.get("/")
def index():
    return {"message":"Hello World"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="ID of student you want to view", gt=0, lt=3)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, age: int):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not Found"}

@app.get("/get-by-name-and-id/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, age: int):
    if students[student_id]["name"]==name:
        return students[student_id]
    return {"Data":"Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error":"Student Exists"}
    students[student_id]=student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdatedStudent):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    if student.name is not None:
        students[student_id].name = student.name
    if student.age is not None:
        students[student_id].age = student.age
    if student.year is not None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    del students[student_id]
    return {"Message":"Student deleted successfully"}