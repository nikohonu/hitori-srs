from lxml import html


def clear_sentence(sentence):
    return html.fromstring(sentence).text_content()


def clear_word(word):
    word = word.replace(".", "")
    word = word.replace(",", "")
    return word
