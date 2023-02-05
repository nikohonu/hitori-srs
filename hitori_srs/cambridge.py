from pathlib import Path

import requests
from bs4 import BeautifulSoup


def get_definition(word: str):
    headers = {"user-agent": "hitori-srs/0.1.0"}
    response = requests.get(
        f"https://dictionary.cambridge.org/dictionary/english/{word}", headers=headers
    )
    html = response.text
    # html = Path("example.html").read_text()
    soup = BeautifulSoup(html, features="lxml")
    result = soup.find_all("div", {"class": "def ddef_d db"})
    definitions = []
    for r in result:
        definition = r.get_text()
        if definition[-2] == ":":
            definition = definition[:-2]
        definition = " ".join(definition.split())
        definitions.append(definition)
    return definitions
