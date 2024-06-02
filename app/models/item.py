# app/models/item.py
from pydantic import BaseModel

class Question(BaseModel):
    question: str
