import requests
from bs4 import BeautifulSoup
import json

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    req = json.loads(req)  # Parse JSON input
    url = req['url']  # Extract URL from JSON

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title of the page
    page_title = soup.title.string

    return page_title
