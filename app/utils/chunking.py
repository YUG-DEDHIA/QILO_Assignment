# app/utils/chunking.py
def chunk_content(content: str, chunk_size: int = 500) -> list:
    return [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
