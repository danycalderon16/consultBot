#Python

# Modules
from chatbot import get_response

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi.middleware.cors import CORSMiddleware

# Models
class Question(BaseModel):
    text: str
    
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home(): 
    res = get_response("como estas?")
    return {"Hello":res}

@app.post("/question")
def create_question(question:Question = Body(...)):
    res = get_response(question.text)
    return res
