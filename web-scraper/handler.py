from bs4 import BeautifulSoup, Comment
import requests
import json

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    response = requests.get(req)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Remove comments
    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()

    # Get page text
    page_text = ' '.join(soup.stripped_strings)

    # Extract title of the page
    page_title = soup.title.string if soup.title else "No title"

    result = {
        'title': page_title,
        'content': page_text,
    }

    return json.dumps(result)
