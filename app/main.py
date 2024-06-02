# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.scraper import scrape_wikipedia
from app.vector_db import chunk_text, store_chunks, retrieve_top_chunks
from app.llm_integration import query_llm

app = FastAPI()

class Question(BaseModel):
    question: str

@app.on_event("startup")
async def startup_event():
    content = scrape_wikipedia("Luke Skywalker")
    chunks = chunk_text(content)
    store_chunks(chunks)

@app.post("/ask")
async def ask_question(question: Question):
    top_chunks = retrieve_top_chunks(question.question)
    context = " ".join(top_chunks)
    answer = query_llm(question.question, context)
    return {"answer": answer}
