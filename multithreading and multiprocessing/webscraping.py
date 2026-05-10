import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# List of URLs
urls = [
    "https://python.langchain.com/docs/introduction/",
    "https://python.langchain.com/docs/tutorials/",
    "https://python.langchain.com/docs/concepts/"
]

# Function to scrape webpage
def scrape(url):

    # Send request
    response = requests.get(url)

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Print length of webpage text
    print(f"{url} -> {len(soup.text)}")


# Multithreading
with ThreadPoolExecutor(max_workers=3) as executor:

    executor.map(scrape, urls)