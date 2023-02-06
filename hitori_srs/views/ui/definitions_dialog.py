# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'definitions_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QGridLayout, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_DefinitionsDialog(object):
    def setupUi(self, DefinitionsDialog):
        if not DefinitionsDialog.objectName():
            DefinitionsDialog.setObjectName(u"DefinitionsDialog")
        DefinitionsDialog.resize(1280, 720)
        DefinitionsDialog.setMinimumSize(QSize(1280, 720))
        self.gridLayout = QGridLayout(DefinitionsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table = QTableWidget(DefinitionsDialog)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setTextElideMode(Qt.ElideMiddle)

        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)

        self.button_box = QDialogButtonBox(DefinitionsDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.button_box, 1, 0, 1, 1)


        self.retranslateUi(DefinitionsDialog)
        self.button_box.accepted.connect(DefinitionsDialog.accept)
        self.button_box.rejected.connect(DefinitionsDialog.reject)

        QMetaObject.connectSlotsByName(DefinitionsDialog)
    # setupUi

    def retranslateUi(self, DefinitionsDialog):
        DefinitionsDialog.setWindowTitle(QCoreApplication.translate("DefinitionsDialog", u"Definitions", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DefinitionsDialog", u"Word", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DefinitionsDialog", u"Definition", None));
    # retranslateUi

