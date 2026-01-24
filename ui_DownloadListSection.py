# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DownloadListSection.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QSizePolicy,
    QWidget)

from DownloadWidgets import DownloadList

class Ui_DownloadListSection(object):
    def setupUi(self, DownloadListSection):
        if not DownloadListSection.objectName():
            DownloadListSection.setObjectName(u"DownloadListSection")
        DownloadListSection.resize(400, 300)
        DownloadListSection.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.list = DownloadList(DownloadListSection)
        self.list.setObjectName(u"list")
        self.list.setGeometry(QRect(3, 22, 395, 276))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy)
        self.list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list.setProperty(u"showDropIndicator", False)
        self.list.setAlternatingRowColors(True)
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.list.setUniformItemSizes(False)

        self.retranslateUi(DownloadListSection)

        QMetaObject.connectSlotsByName(DownloadListSection)
    # setupUi

    def retranslateUi(self, DownloadListSection):
        DownloadListSection.setWindowTitle(QCoreApplication.translate("DownloadListSection", u"GroupBox", None))
        DownloadListSection.setTitle(QCoreApplication.translate("DownloadListSection", u"Placing my holder so much", None))
    # retranslateUi

