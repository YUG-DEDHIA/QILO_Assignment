# app/api.py
from fastapi import APIRouter
from app.scraper import scrape_wikipedia
from app.vector_db import store_chunks, retrieve_top_chunks
from app.llm_integration import query_llm
from app.models.item import Question
from app.utils.chunking import chunk_content

router = APIRouter()

@router.post("/scrape")
async def scrape_page():
    content = scrape_wikipedia("https://en.wikipedia.org/wiki/Luke_Skywalker")
    chunks = chunk_content(content)
    store_chunks(chunks)
    return {"message": "Page scraped and stored in vector database"}

@router.post("/ask")
async def ask_question(question: Question):
    top_chunks = retrieve_top_chunks(question.question)
    context = " ".join(top_chunks)
    answer = query_llm(question.question, context)
    return {"answer": answer}
