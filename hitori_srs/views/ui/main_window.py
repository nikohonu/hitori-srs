# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 320)
        MainWindow.setMinimumSize(QSize(640, 320))
        self.action_add_word = QAction(MainWindow)
        self.action_add_word.setObjectName(u"action_add_word")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.text_translated_sentence = QTextEdit(self.centralwidget)
        self.text_translated_sentence.setObjectName(u"text_translated_sentence")

        self.gridLayout.addWidget(self.text_translated_sentence, 1, 1, 1, 1)

        self.text_sentence = QTextEdit(self.centralwidget)
        self.text_sentence.setObjectName(u"text_sentence")

        self.gridLayout.addWidget(self.text_sentence, 1, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.text_word = QTextEdit(self.centralwidget)
        self.text_word.setObjectName(u"text_word")

        self.gridLayout.addWidget(self.text_word, 3, 0, 1, 1)

        self.text_definition = QTextEdit(self.centralwidget)
        self.text_definition.setObjectName(u"text_definition")

        self.gridLayout.addWidget(self.text_definition, 3, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuEdit.addAction(self.action_add_word)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"hitori_srs", None))
        self.action_add_word.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(shortcut)
        self.action_add_word.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sentence", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Word", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Word", None))
    # retranslateUi

