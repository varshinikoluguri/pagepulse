import requests
from bs4 import BeautifulSoup
import time


def analyze_url(url):
    try:
        # Start timer
        start_time = time.time()

        # Fetch the webpage
        response = requests.get(
    url,
    timeout=10,
    headers={
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.9",
    }
)
        # Stop timer
        response_time = round((time.time() - start_time) * 1000, 2)

        # Check if the response is HTML
        content_type = response.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            return {
                "error": "The URL does not contain an HTML page."
            }

        # Parse HTML
        soup = BeautifulSoup(response.text, "lxml")

        # Page title
        title = soup.title.string.strip() if soup.title else "No Title"

        # Meta description
        meta = soup.find("meta", attrs={"name": "description"})
        meta_description = (
            meta.get("content").strip()
            if meta and meta.get("content")
            else "No Meta Description"
        )

        # H1 count
        h1_count = len(soup.find_all("h1"))

        # Images without alt
        images = soup.find_all("img")
        missing_alt = sum(
            1 for img in images if not img.get("alt")
        )

        # Word count
        text = soup.get_text(separator=" ", strip=True)
        word_count = len(text.split())

        return {
            "status": response.status_code,
            "response_time_ms": response_time,
            "title": title,
            "meta_description": meta_description,
            "h1_count": h1_count,
            "images_without_alt": missing_alt,
            "word_count": word_count
        }

    except requests.exceptions.RequestException:
        return {
            "error": "Unable to fetch the URL."
        }