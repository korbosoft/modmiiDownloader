# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import rc_resource

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 400)
        icon = QIcon()
        icon.addFile(u":/base/mainIcon", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.ok = QPushButton(Dialog)
        self.ok.setObjectName(u"ok")
        self.ok.setGeometry(QRect(320, 360, 80, 30))
        self.reset = QPushButton(Dialog)
        self.reset.setObjectName(u"reset")
        self.reset.setGeometry(QRect(240, 360, 80, 30))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 0, 400, 30))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Search", None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.reset.setText(QCoreApplication.translate("Dialog", u"Reset", None))
    # retranslateUi

