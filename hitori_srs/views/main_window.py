from pattern.text.en import singularize
from PySide6.QtWidgets import QMainWindow
from translatepy.translators.google import GoogleTranslate

from hitori_srs.views.ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, language, sentence) -> None:
        super().__init__()
        self.setupUi(self)
        self.language = language
        self.text_sentence.setPlainText(sentence)
        self.google = GoogleTranslate()
        translated_sentence = self.google.translate(sentence, self.language).result
        self.text_translated_sentence.setPlainText(translated_sentence)
        self.action_add_word.triggered.connect(self.add_word)

    def add_word(self):
        word = self.text_sentence.textCursor().selectedText()
        if word:
            word = word.lower()
            word = singularize(word)
            self.edit_word.setText(word)
            translated_word = self.google.translate(word, self.language).result
            self.edit_translated_word.setText(translated_word)
