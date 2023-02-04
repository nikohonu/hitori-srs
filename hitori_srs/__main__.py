import sys

import click
from PySide6.QtWidgets import QApplication

from hitori_srs.views.main_window import MainWindow


@click.command()
@click.argument("language")
@click.argument("sentence")
def main(language, sentence):
    app = QApplication(sys.argv)
    window = MainWindow(language, sentence)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
