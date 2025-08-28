import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

BASE_URL = "https://wca.edu.pk/"
PAGES = [
    "",  # Home
    "Academics",
    "Admissions",
    "Examinations",
    "Lectures",
    "Map",
    "ContactUs",
    "AboutUS",
    "Mission",
    "Introduction"
]
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
def get_page_text(url):
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, "lxml")
        # Remove scripts/styles/nav/footer/header/form
        for tag in soup(["script", "style", "nav", "footer", "header", "form"]):
            tag.decompose()
        # Get visible text
        text = soup.get_text(separator="\n", strip=True)
        # Remove empty lines
        lines = [line for line in text.splitlines() if line.strip()]
        return "\n".join(lines)
    except Exception as e:
        return f"Error fetching {url}: {e}"

knowledge_base = {}

for page in PAGES:
    url = urljoin(BASE_URL, page)
    text = get_page_text(url)
    key = page if page else "Home"
    knowledge_base[key] = text[:2000]  # Limit to 2000 chars per section for brevity

# Save to JSON
with open("knowledge_base.json", "w", encoding="utf-8") as f:
    json.dump(knowledge_base, f, indent=2, ensure_ascii=False)

print("Knowledge base created as knowledge_base.json") 