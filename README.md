# QILO_Assignment
# RAG Application

This RAG application provides answers to questions about Luke Skywalker using data scraped from Wikipedia, stored in a vector database, and queried using the LLaMA 3 70B Instruct model.

## Features

1. Scrape the "Luke Skywalker" Wikipedia page.
2. Chunk the content and store it in a Faiss vector database.
3. Call an LLM API (LLaMA 3 70B Instruct).
4. Ask questions via a REST API.
5. Retrieve the top 3 relevant chunks from the vector database.
6. Pass the question along with the retrieved chunks to the LLM.
7. Return the generated answer.
