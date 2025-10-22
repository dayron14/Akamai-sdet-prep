import requests

def get_status_code(url: str) -> int:
    """Return the HTTP status code for a given URL."""
    response = requests.get(url)
    return response.status_code


def get_json_placeholder_post(post_id: int) -> dict:
    """Fetch a post from the public JSONPlaceholder API."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    response.raise_for_status()   # raises HTTPError for bad responses
    return response.json()
