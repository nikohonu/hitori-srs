from lxml import html
from pattern.text.en import Sentence, singularize
from PySide6.QtWidgets import QMainWindow
from translatepy.translators.google import GoogleTranslate

from hitori_srs.views.ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, language, sentence) -> None:
        super().__init__()
        self.setupUi(self)
        self.language = language
        self.text_sentence.setText(sentence)
        self.google = GoogleTranslate()
        self.translate()
        self.action_add_word.triggered.connect(self.add_word)

    def translate(self):
        sentence = html.fromstring(self.text_sentence.toPlainText()).text_content()
        translated_sentence = self.google.translate(sentence, self.language).result
        self.text_translated_sentence.setText(translated_sentence)

    def clear_word(self, word):
        word = word.replace(".", "")
        word = word.replace(",", "")
        return word

    def highlight_word(self, words):
        sentence = html.fromstring(self.text_sentence.toPlainText()).text_content()
        sentence_words = sentence.split()
        result = []
        for sentence_word in sentence_words:
            if self.clear_word(sentence_word) in words:
                result.append(
                    f'<span style="color: rgb(0, 0, 255);">{sentence_word}</span>'
                )
            else:
                result.append(sentence_word)
        sentence = " ".join(result)
        self.text_sentence.setText(sentence)

    def add_word(self):
        word = self.text_sentence.textCursor().selectedText()
        if word:
            words_for_highlighting = {word}
            word = word.lower()
            words_for_highlighting.add(word)
            word = singularize(word)
            words_for_highlighting.add(word)
            self.highlight_word(words_for_highlighting)
            self.edit_word.setText(word)
            translated_word = self.google.translate(word, self.language).result
            self.edit_translated_word.setText(translated_word)
