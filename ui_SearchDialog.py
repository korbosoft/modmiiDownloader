# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

from downloadWidgets import DownloadListSection
import rc_resource

class Ui_SearchDialog(object):
    def setupUi(self, SearchDialog):
        if not SearchDialog.objectName():
            SearchDialog.setObjectName(u"SearchDialog")
        SearchDialog.resize(400, 400)
        icon = QIcon()
        icon.addFile(u":/base/mainIcon", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SearchDialog.setWindowIcon(icon)
        self.add = QPushButton(SearchDialog)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(0, 30, 200, 30))
        self.remove = QPushButton(SearchDialog)
        self.remove.setObjectName(u"remove")
        self.remove.setGeometry(QRect(200, 30, 200, 30))
        self.query = QLineEdit(SearchDialog)
        self.query.setObjectName(u"query")
        self.query.setGeometry(QRect(0, 0, 320, 30))
        self.query.setClearButtonEnabled(True)
        self.ok = QPushButton(SearchDialog)
        self.ok.setObjectName(u"ok")
        self.ok.setGeometry(QRect(200, 370, 200, 30))
        self.cancel = QPushButton(SearchDialog)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(0, 370, 200, 30))
        self.horizontalLayoutWidget = QWidget(SearchDialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 60, 400, 310))
        self.layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.results = DownloadListSection(self.horizontalLayoutWidget)
        self.results.setObjectName(u"results")
        self.results.setEnabled(True)
        self.results.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.results)

        self.queue = DownloadListSection(self.horizontalLayoutWidget)
        self.queue.setObjectName(u"queue")
        self.queue.setEnabled(True)
        self.queue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.queue)

        self.search = QPushButton(SearchDialog)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(320, 0, 80, 30))
        icon1 = QIcon()
        icon1.addFile(u":/base/svg_ios", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search.setIcon(icon1)

        self.retranslateUi(SearchDialog)

        self.cancel.setDefault(True)


        QMetaObject.connectSlotsByName(SearchDialog)
    # setupUi

    def retranslateUi(self, SearchDialog):
        SearchDialog.setWindowTitle(QCoreApplication.translate("SearchDialog", u"Search", None))
        self.add.setText(QCoreApplication.translate("SearchDialog", u"Add Selected", None))
        self.remove.setText(QCoreApplication.translate("SearchDialog", u"Remove Selected", None))
        self.query.setPlaceholderText(QCoreApplication.translate("SearchDialog", u"Search", None))
        self.ok.setText(QCoreApplication.translate("SearchDialog", u"OK", None))
        self.cancel.setText(QCoreApplication.translate("SearchDialog", u"Cancel", None))
        self.results.setTitle(QCoreApplication.translate("SearchDialog", u"Results", None))
        self.queue.setTitle(QCoreApplication.translate("SearchDialog", u"Queue", None))
        self.search.setText(QCoreApplication.translate("SearchDialog", u"Search", None))
    # retranslateUi

