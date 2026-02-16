from fastapi import FastAPI
from pydantic import BaseModel
from agent.core import run_agent
from agent.memory import get

app = FastAPI(title="AI Dev Agent Platform")

class Request(BaseModel):
    task: str
    input: str


@app.post("/agent")
def agent(req: Request):
    result = run_agent(req.task, req.input)
    return {"response": result}


@app.get("/memory")
def memory():
    return {"history": get()}
