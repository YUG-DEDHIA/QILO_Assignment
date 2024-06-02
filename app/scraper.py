# app/scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.get_text()
