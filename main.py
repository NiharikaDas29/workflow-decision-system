from fastapi import FastAPI
from workflow_engine import run_workflow

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Workflow Decision System Running"}


@app.post("/process")

def process(data: dict):

    result = run_workflow(data)

    return result
