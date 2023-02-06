from PySide6.QtWidgets import QDialog, QTableWidgetItem, QTabWidget

import hitori_srs.cambridge as cambridge
import hitori_srs.e2u as e2u
from hitori_srs import cambridge
from hitori_srs.views.ui.definitions_dialog import Ui_DefinitionsDialog


class DefinitionsDialog(QDialog, Ui_DefinitionsDialog):
    def __init__(self, word) -> None:
        super().__init__()
        self.setupUi(self)
        dictionaries = cambridge.get_definition(word)
        dictionaries.extend(e2u.get_definition(word))
        print(dictionaries)

        self.table.setRowCount(len(dictionaries))
        for i in range(len(dictionaries)):
            for j in range(2):
                self.table.setItem(i, j, QTableWidgetItem(dictionaries[i][j]))
        self.table.resizeRowsToContents()
        self.table.itemDoubleClicked.connect(self.accept)
        self.table.setWordWrap(True)
        self.table.resizeColumnToContents(0)
        self.table.setColumnWidth(1, 800)
        self.table.resizeRowsToContents()

    def get_selected(self):
        word, definition = self.table.selectedItems()
        word = word.text()
        definition = definition.text()
        return word, definition
