from pattern.text.en import singularize
from PySide6.QtWidgets import QMainWindow
from translatepy.translators.google import GoogleTranslate

from hitori_srs.text import clear_sentence, clear_word
from hitori_srs.views.definitions_dialog import DefinitionsDialog
from hitori_srs.views.ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, language, sentence) -> None:
        super().__init__()
        self.setupUi(self)
        self.language = language
        self.google = GoogleTranslate()
        self.text_sentence.setText(clear_sentence(sentence))
        self.translate()
        self.action_add_word.triggered.connect(self.add_word)

    def translate(self):
        sentence = clear_sentence(self.text_sentence.toPlainText())
        translated_sentence = self.google.translate(sentence, self.language).result
        self.text_translated_sentence.setText(translated_sentence)

    def highlight_word(self, words):
        sentence = clear_sentence(self.text_sentence.toPlainText())
        sentence = " ".join(sentence.split())
        for word in words:
            sentence = sentence.replace(word, f'<span style="color: rgb(0, 0, 255);">{word}</span>')
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
            self.text_word.setText(word)
            dd = DefinitionsDialog(word)
            if dd.exec():
                word, definition = dd.get_selected()
                self.text_word.setText(word)
                self.text_definition.setText(definition)

            # translated_word = self.google.translate(word, self.language).result
            # self.edit_translated_word.setText(translated_word)
