from pathlib import Path

import lxml
import requests
from bs4 import BeautifulSoup
from click import parser


def get_definition(word: str):
    headers = {"user-agent": "hitori-srs/0.1.0"}
    response = requests.get(
        f"https://e2u.org.ua/s?w={word}&dicts=17&main_only=on&highlight=on",
        headers=headers,
    )
    html = response.text
    # html = Path("example.html").read_text()
    soup = BeautifulSoup(html, features="lxml")
    result = soup.find_all("td", {"class": "result_row_main"})
    definitions = []

    def get_definition_from_row(html_row, word):
        result = []
        for tag_str in html_row.contents:
            tag_str = str(tag_str).strip()
            if not tag_str:
                continue
            tag = BeautifulSoup(tag_str, features="html.parser")
            if not bool(tag.find()) or (bool(tag.find("i")) and len(tag.text) > 1):
                result.append(tag)
        return (
            " ".join(str(t.text) for t in result)
            .replace("( ", "(")
            .replace(" )", ")")
            .replace(" ◊", "")
        )

    def get_word_definition(row, word):
        html_row = BeautifulSoup(
            "".join(str(t).strip() for t in row).strip(), features="html.parser"
        )
        if not html_row.b:
            return
        local_word = html_row.b.text.strip()
        if local_word != word:
            local_word = (
                word if local_word[-1] == "." else local_word.replace("~", word)
            )
            return local_word, get_definition_from_row(html_row, word)

    for r in result:
        word = r.b.text
        tags = r.contents
        row = []
        rows = []
        while tags:
            tag = tags.pop(0)
            if str(tag).find("br") == -1:
                row.append(tag)
            else:
                rows.append(row)
                row = []
                continue
        rows.append(row)
        if len(rows) > 1:
            local_definitions = []
            for row in rows:
                r = get_word_definition(row, word)
                if r:
                    local_definitions.append(r)
            definitions.extend(local_definitions)
        else:
            definitions.append((word, row[-1].strip()))
    return definitions
