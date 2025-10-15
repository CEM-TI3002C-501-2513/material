import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

class StudentModel(BaseModel):
    nombre: str
    matrícula: int
    email: str
    carrera: str | None

def load_data():
    df = pd.read_csv("exams.csv")
    return df

app = FastAPI()

@app.get("/")
def get_home():
    return "Hola mundo"

@app.get("/gender")
def get_gender():
    df = load_data()
    return df["gender"].value_counts().reset_index().to_dict(orient="records")

# Path Parameters
@app.get("/race/{group}")
def get_race(group: str):
    group = group.upper()
    if group not in ["A", "B", "C", "D", "E"]:
        return {"error": "No encontrado"}
    df = load_data()
    return {
        "math score": df.loc[df["race/ethnicity"] == f"group {group}", "math score"].mean(),
        "reading score": df.loc[df["race/ethnicity"] == f"group {group}", "reading score"].mean(),
        "writing score": df.loc[df["race/ethnicity"] == f"group {group}", "writing score"].mean()
    }
    
@app.get("/top_scores")
def get_top_scores(exam: str = "math"):
    exam = exam if exam in ["math", "reading", "writing"] else "math"
    df = load_data()
    return {"scores": df[f"{exam} score"].nlargest(5).to_dict()}

@app.post("/new_student")
def post_new_student(student: StudentModel):
    return {"mensaje": f"Bienvenid@ {student.nombre} con matrícula {student.matrícula}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)