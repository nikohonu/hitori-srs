from pathlib import Path

import requests
from bs4 import BeautifulSoup


def get_definition(word: str):
    headers = {"user-agent": "hitori-srs/0.1.0"}
    response = requests.get(
        f"https://dictionary.cambridge.org/dictionary/english/{word}", headers=headers
    )
    html = response.text
    # print(html)
    # return
    # html = Path("example.html").read_text()
    soup = BeautifulSoup(html, features="lxml")
    definitions = []
    for dict_ in soup.find_all("div", {"class": "pr dictionary"}):
        # entry
        for entry in dict_.find_all("div", {"class": "entry"}):
            word = entry.find("div", {"class": "di-title"}).text
            entry_bodies = list(entry.find_all("div", {"class": "pr entry-body__el"}))
            entry_bodies.extend(
                entry.find_all("div", {"class": "entry-body__el clrd js-share-holder"})
            )
            for entry_body in entry_bodies:
                pr_dsenses = list(entry_body.find_all("div", {"class": "pr dsense"}))
                pr_dsenses.extend(
                    entry_body.find_all("div", {"class": "pr dsense dsense-noh"})
                )
                for pr_dsense in pr_dsenses:
                    guide_word = pr_dsense.find(
                        "span", {"class": "guideword dsense_gw"}
                    )
                    if guide_word:
                        guide_word = guide_word.text.strip()
                    sense_body = pr_dsense.find("div", {"class": "sense-body dsense_b"})
                    for def_block in sense_body.find_all("div", recursive=False):
                        phrase = def_block.find(
                            "span", {"class": "phrase-title dphrase-title"}
                        )
                        if phrase:
                            local_word = phrase.text.strip()
                        else:
                            local_word = word
                        try:
                            definition = str(
                                def_block.find("div", {"class": "def ddef_d db"}).text
                            )
                            if definition[-2] == ":":
                                definition = definition[:-2]
                            if guide_word:
                                definitions.append(
                                    (f"{local_word} {guide_word}", definition)
                                )
                            else:
                                definitions.append((local_word, definition))
                        except:
                            pass
        # idiom
        idiom = dict_.find("div", {"class": "pr idiom-block"})
        if not idiom:
            continue
        word = idiom.find("div", {"class": "di-title"}).text
        for idiom_body in idiom.find_all("span", {"class": "idiom-body didiom-body"}):
            definition = str(idiom_body.find("div", {"class": "def ddef_d db"}).text)
            if definition[-2] == ":":
                definition = definition[:-2]
            definitions.append((word, definition))
    return definitions
