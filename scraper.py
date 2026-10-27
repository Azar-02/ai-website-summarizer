
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def fetch_website_contents(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=15
        )
        response.raise_for_status()

    except requests.exceptions.RequestException as error:
        raise ValueError(
            f"Could not fetch the website: {error}"
        ) from error

    soup = BeautifulSoup(response.text, "html.parser")

    title = (
        soup.title.get_text(strip=True)
        if soup.title
        else "No title found"
    )

    for tag in soup([
        "script", "style", "nav", "footer",
        "header", "img", "input"
    ]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)

    if not text:
        raise ValueError("No readable content found.")

    return f"Title: {title}\n\nPage contents:\n{text}"


if __name__ == "__main__":
    try:
        website = fetch_website_contents("https://example.com")
        print(website[:2000])

    except ValueError as error:
        print(error)
