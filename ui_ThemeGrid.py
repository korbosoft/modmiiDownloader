# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ThemeGrid.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QPushButton,
    QSizePolicy, QWidget)

class Ui_ThemeGrid(object):
    def setupUi(self, ThemeGrid):
        if not ThemeGrid.objectName():
            ThemeGrid.setObjectName(u"ThemeGrid")
        ThemeGrid.resize(800, 630)
        ThemeGrid.setStyleSheet(u"QCheckBox {\n"
"	spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	subcontrol-position: top center;\n"
"	width: 32px;\n"
"	height: 32px;\n"
"}")
        self.widget = QWidget(ThemeGrid)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 800, 630))
        self.layout = QGridLayout(self.widget)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.s43E = QPushButton(self.widget)
        self.s43E.setObjectName(u"s43E")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s43E.sizePolicy().hasHeightForWidth())
        self.s43E.setSizePolicy(sizePolicy)
        self.s43E.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.s43E, 4, 0, 1, 1)

        self.O_43U = QCheckBox(self.widget)
        self.O_43U.setObjectName(u"O_43U")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.O_43U.sizePolicy().hasHeightForWidth())
        self.O_43U.setSizePolicy(sizePolicy1)
        self.O_43U.setStyleSheet(u"")

        self.layout.addWidget(self.O_43U, 1, 1, 1, 1)

        self.O_42E = QCheckBox(self.widget)
        self.O_42E.setObjectName(u"O_42E")
        sizePolicy1.setHeightForWidth(self.O_42E.sizePolicy().hasHeightForWidth())
        self.O_42E.setSizePolicy(sizePolicy1)
        self.O_42E.setStyleSheet(u"")

        self.layout.addWidget(self.O_42E, 5, 1, 1, 1)

        self.s43U = QPushButton(self.widget)
        self.s43U.setObjectName(u"s43U")
        sizePolicy.setHeightForWidth(self.s43U.sizePolicy().hasHeightForWidth())
        self.s43U.setSizePolicy(sizePolicy)
        self.s43U.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.s43U, 1, 0, 1, 1)

        self.c = QPushButton(self.widget)
        self.c.setObjectName(u"c")
        sizePolicy.setHeightForWidth(self.c.sizePolicy().hasHeightForWidth())
        self.c.setSizePolicy(sizePolicy)
        self.c.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.c, 0, 3, 1, 1)

        self.DarkWii_Blue_43U = QCheckBox(self.widget)
        self.DarkWii_Blue_43U.setObjectName(u"DarkWii_Blue_43U")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_43U.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_43U.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_43U.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_43U, 1, 4, 1, 1)

        self.O_vU = QCheckBox(self.widget)
        self.O_vU.setObjectName(u"O_vU")
        sizePolicy1.setHeightForWidth(self.O_vU.sizePolicy().hasHeightForWidth())
        self.O_vU.setSizePolicy(sizePolicy1)
        self.O_vU.setStyleSheet(u"")

        self.layout.addWidget(self.O_vU, 13, 1, 1, 1)

        self.s42J = QPushButton(self.widget)
        self.s42J.setObjectName(u"s42J")
        sizePolicy.setHeightForWidth(self.s42J.sizePolicy().hasHeightForWidth())
        self.s42J.setSizePolicy(sizePolicy)
        self.s42J.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.s42J, 8, 0, 1, 1)

        self.g = QPushButton(self.widget)
        self.g.setObjectName(u"g")
        sizePolicy.setHeightForWidth(self.g.sizePolicy().hasHeightForWidth())
        self.g.setSizePolicy(sizePolicy)
        self.g.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.g, 0, 7, 1, 1)

        self.s41J = QPushButton(self.widget)
        self.s41J.setObjectName(u"s41J")
        sizePolicy.setHeightForWidth(self.s41J.sizePolicy().hasHeightForWidth())
        self.s41J.setSizePolicy(sizePolicy)
        self.s41J.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.s41J, 9, 0, 1, 1)

        self.O_42K = QCheckBox(self.widget)
        self.O_42K.setObjectName(u"O_42K")
        sizePolicy1.setHeightForWidth(self.O_42K.sizePolicy().hasHeightForWidth())
        self.O_42K.setSizePolicy(sizePolicy1)
        self.O_42K.setStyleSheet(u"")

        self.layout.addWidget(self.O_42K, 11, 1, 1, 1)

        self.e = QPushButton(self.widget)
        self.e.setObjectName(u"e")
        sizePolicy.setHeightForWidth(self.e.sizePolicy().hasHeightForWidth())
        self.e.setSizePolicy(sizePolicy)
        self.e.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.e, 0, 5, 1, 1)

        self.O_41U = QCheckBox(self.widget)
        self.O_41U.setObjectName(u"O_41U")
        sizePolicy1.setHeightForWidth(self.O_41U.sizePolicy().hasHeightForWidth())
        self.O_41U.setSizePolicy(sizePolicy1)
        self.O_41U.setStyleSheet(u"")

        self.layout.addWidget(self.O_41U, 3, 1, 1, 1)

        self.d = QPushButton(self.widget)
        self.d.setObjectName(u"d")
        sizePolicy.setHeightForWidth(self.d.sizePolicy().hasHeightForWidth())
        self.d.setSizePolicy(sizePolicy)
        self.d.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.d, 0, 4, 1, 1)

        self.s41K = QPushButton(self.widget)
        self.s41K.setObjectName(u"s41K")
        sizePolicy.setHeightForWidth(self.s41K.sizePolicy().hasHeightForWidth())
        self.s41K.setSizePolicy(sizePolicy)
        self.s41K.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.s41K, 12, 0, 1, 1)

        self.DarkWii_Green_43U_W = QCheckBox(self.widget)
        self.DarkWii_Green_43U_W.setObjectName(u"DarkWii_Green_43U_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_43U_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_43U_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_43U_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_43U_W, 1, 7, 1, 1)

        self.O_41J = QCheckBox(self.widget)
        self.O_41J.setObjectName(u"O_41J")
        sizePolicy1.setHeightForWidth(self.O_41J.sizePolicy().hasHeightForWidth())
        self.O_41J.setSizePolicy(sizePolicy1)
        self.O_41J.setStyleSheet(u"")

        self.layout.addWidget(self.O_41J, 9, 1, 1, 1)

        self.O_43K = QCheckBox(self.widget)
        self.O_43K.setObjectName(u"O_43K")
        sizePolicy1.setHeightForWidth(self.O_43K.sizePolicy().hasHeightForWidth())
        self.O_43K.setSizePolicy(sizePolicy1)
        self.O_43K.setStyleSheet(u"")

        self.layout.addWidget(self.O_43K, 10, 1, 1, 1)

        self.svU = QPushButton(self.widget)
        self.svU.setObjectName(u"svU")
        sizePolicy.setHeightForWidth(self.svU.sizePolicy().hasHeightForWidth())
        self.svU.setSizePolicy(sizePolicy)
        self.svU.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.svU, 13, 0, 1, 1)

        self.youtube = QPushButton(self.widget)
        self.youtube.setObjectName(u"youtube")
        sizePolicy.setHeightForWidth(self.youtube.sizePolicy().hasHeightForWidth())
        self.youtube.setSizePolicy(sizePolicy)
        self.youtube.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.youtube, 0, 0, 1, 1)

        self.DarkWii_Orange_43U = QCheckBox(self.widget)
        self.DarkWii_Orange_43U.setObjectName(u"DarkWii_Orange_43U")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_43U.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_43U.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_43U.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_43U, 1, 5, 1, 1)

        self.O_41E = QCheckBox(self.widget)
        self.O_41E.setObjectName(u"O_41E")
        sizePolicy1.setHeightForWidth(self.O_41E.sizePolicy().hasHeightForWidth())
        self.O_41E.setSizePolicy(sizePolicy1)
        self.O_41E.setStyleSheet(u"")

        self.layout.addWidget(self.O_41E, 6, 1, 1, 1)

        self.s42K = QPushButton(self.widget)
        self.s42K.setObjectName(u"s42K")
        sizePolicy.setHeightForWidth(self.s42K.sizePolicy().hasHeightForWidth())
        self.s42K.setSizePolicy(sizePolicy)
        self.s42K.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.s42K, 11, 0, 1, 1)

        self.DarkWii_Red_43U_W = QCheckBox(self.widget)
        self.DarkWii_Red_43U_W.setObjectName(u"DarkWii_Red_43U_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_43U_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_43U_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_43U_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_43U_W, 1, 6, 1, 1)

        self.s43J = QPushButton(self.widget)
        self.s43J.setObjectName(u"s43J")
        sizePolicy.setHeightForWidth(self.s43J.sizePolicy().hasHeightForWidth())
        self.s43J.setSizePolicy(sizePolicy)
        self.s43J.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.s43J, 7, 0, 1, 1)

        self.b = QPushButton(self.widget)
        self.b.setObjectName(u"b")
        sizePolicy.setHeightForWidth(self.b.sizePolicy().hasHeightForWidth())
        self.b.setSizePolicy(sizePolicy)
        self.b.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.b, 0, 2, 1, 1)

        self.s41U = QPushButton(self.widget)
        self.s41U.setObjectName(u"s41U")
        sizePolicy.setHeightForWidth(self.s41U.sizePolicy().hasHeightForWidth())
        self.s41U.setSizePolicy(sizePolicy)
        self.s41U.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.s41U, 3, 0, 1, 1)

        self.O_43J = QCheckBox(self.widget)
        self.O_43J.setObjectName(u"O_43J")
        sizePolicy1.setHeightForWidth(self.O_43J.sizePolicy().hasHeightForWidth())
        self.O_43J.setSizePolicy(sizePolicy1)
        self.O_43J.setStyleSheet(u"")

        self.layout.addWidget(self.O_43J, 7, 1, 1, 1)

        self.f = QPushButton(self.widget)
        self.f.setObjectName(u"f")
        sizePolicy.setHeightForWidth(self.f.sizePolicy().hasHeightForWidth())
        self.f.setSizePolicy(sizePolicy)
        self.f.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.f, 0, 6, 1, 1)

        self.O_42U = QCheckBox(self.widget)
        self.O_42U.setObjectName(u"O_42U")
        sizePolicy1.setHeightForWidth(self.O_42U.sizePolicy().hasHeightForWidth())
        self.O_42U.setSizePolicy(sizePolicy1)
        self.O_42U.setStyleSheet(u"")

        self.layout.addWidget(self.O_42U, 2, 1, 1, 1)

        self.O_43E = QCheckBox(self.widget)
        self.O_43E.setObjectName(u"O_43E")
        sizePolicy1.setHeightForWidth(self.O_43E.sizePolicy().hasHeightForWidth())
        self.O_43E.setSizePolicy(sizePolicy1)
        self.O_43E.setStyleSheet(u"")

        self.layout.addWidget(self.O_43E, 4, 1, 1, 1)

        self.s41E = QPushButton(self.widget)
        self.s41E.setObjectName(u"s41E")
        sizePolicy.setHeightForWidth(self.s41E.sizePolicy().hasHeightForWidth())
        self.s41E.setSizePolicy(sizePolicy)
        self.s41E.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.s41E, 6, 0, 1, 1)

        self.i = QPushButton(self.widget)
        self.i.setObjectName(u"i")
        sizePolicy.setHeightForWidth(self.i.sizePolicy().hasHeightForWidth())
        self.i.setSizePolicy(sizePolicy)
        self.i.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.i, 0, 9, 1, 1)

        self.s42U = QPushButton(self.widget)
        self.s42U.setObjectName(u"s42U")
        sizePolicy.setHeightForWidth(self.s42U.sizePolicy().hasHeightForWidth())
        self.s42U.setSizePolicy(sizePolicy)
        self.s42U.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.s42U, 2, 0, 1, 1)

        self.s43K = QPushButton(self.widget)
        self.s43K.setObjectName(u"s43K")
        sizePolicy.setHeightForWidth(self.s43K.sizePolicy().hasHeightForWidth())
        self.s43K.setSizePolicy(sizePolicy)
        self.s43K.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.s43K, 10, 0, 1, 1)

        self.svJ = QPushButton(self.widget)
        self.svJ.setObjectName(u"svJ")
        sizePolicy.setHeightForWidth(self.svJ.sizePolicy().hasHeightForWidth())
        self.svJ.setSizePolicy(sizePolicy)
        self.svJ.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.svJ, 15, 0, 1, 1)

        self.h = QPushButton(self.widget)
        self.h.setObjectName(u"h")
        sizePolicy.setHeightForWidth(self.h.sizePolicy().hasHeightForWidth())
        self.h.setSizePolicy(sizePolicy)
        self.h.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.h, 0, 8, 1, 1)

        self.O_42J = QCheckBox(self.widget)
        self.O_42J.setObjectName(u"O_42J")
        sizePolicy1.setHeightForWidth(self.O_42J.sizePolicy().hasHeightForWidth())
        self.O_42J.setSizePolicy(sizePolicy1)
        self.O_42J.setStyleSheet(u"")

        self.layout.addWidget(self.O_42J, 8, 1, 1, 1)

        self.DarkWii_Red_43U = QCheckBox(self.widget)
        self.DarkWii_Red_43U.setObjectName(u"DarkWii_Red_43U")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_43U.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_43U.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_43U.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_43U, 1, 2, 1, 1)

        self.DarkWii_Green_43U = QCheckBox(self.widget)
        self.DarkWii_Green_43U.setObjectName(u"DarkWii_Green_43U")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_43U.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_43U.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_43U.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_43U, 1, 3, 1, 1)

        self.DarkWii_Blue_43U_W = QCheckBox(self.widget)
        self.DarkWii_Blue_43U_W.setObjectName(u"DarkWii_Blue_43U_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_43U_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_43U_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_43U_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_43U_W, 1, 8, 1, 1)

        self.O_vJ = QCheckBox(self.widget)
        self.O_vJ.setObjectName(u"O_vJ")
        sizePolicy1.setHeightForWidth(self.O_vJ.sizePolicy().hasHeightForWidth())
        self.O_vJ.setSizePolicy(sizePolicy1)
        self.O_vJ.setStyleSheet(u"")

        self.layout.addWidget(self.O_vJ, 15, 1, 1, 1)

        self.a = QPushButton(self.widget)
        self.a.setObjectName(u"a")
        sizePolicy.setHeightForWidth(self.a.sizePolicy().hasHeightForWidth())
        self.a.setSizePolicy(sizePolicy)
        self.a.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.a, 0, 1, 1, 1)

        self.s42E = QPushButton(self.widget)
        self.s42E.setObjectName(u"s42E")
        sizePolicy.setHeightForWidth(self.s42E.sizePolicy().hasHeightForWidth())
        self.s42E.setSizePolicy(sizePolicy)
        self.s42E.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.s42E, 5, 0, 1, 1)

        self.O_41K = QCheckBox(self.widget)
        self.O_41K.setObjectName(u"O_41K")
        sizePolicy1.setHeightForWidth(self.O_41K.sizePolicy().hasHeightForWidth())
        self.O_41K.setSizePolicy(sizePolicy1)
        self.O_41K.setStyleSheet(u"")

        self.layout.addWidget(self.O_41K, 12, 1, 1, 1)

        self.O_vE = QCheckBox(self.widget)
        self.O_vE.setObjectName(u"O_vE")
        sizePolicy1.setHeightForWidth(self.O_vE.sizePolicy().hasHeightForWidth())
        self.O_vE.setSizePolicy(sizePolicy1)
        self.O_vE.setStyleSheet(u"")

        self.layout.addWidget(self.O_vE, 14, 1, 1, 1)

        self.svE = QPushButton(self.widget)
        self.svE.setObjectName(u"svE")
        sizePolicy.setHeightForWidth(self.svE.sizePolicy().hasHeightForWidth())
        self.svE.setSizePolicy(sizePolicy)
        self.svE.setStyleSheet(u"QPushButton { padding: 3px;}")

        self.layout.addWidget(self.svE, 14, 0, 1, 1)

        self.DarkWii_Orange_43U_W = QCheckBox(self.widget)
        self.DarkWii_Orange_43U_W.setObjectName(u"DarkWii_Orange_43U_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_43U_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_43U_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_43U_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_43U_W, 1, 9, 1, 1)

        self.DarkWii_Red_42U = QCheckBox(self.widget)
        self.DarkWii_Red_42U.setObjectName(u"DarkWii_Red_42U")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_42U.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_42U.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_42U.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_42U, 2, 2, 1, 1)

        self.DarkWii_Red_41U = QCheckBox(self.widget)
        self.DarkWii_Red_41U.setObjectName(u"DarkWii_Red_41U")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_41U.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_41U.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_41U.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_41U, 3, 2, 1, 1)

        self.DarkWii_Red_43E = QCheckBox(self.widget)
        self.DarkWii_Red_43E.setObjectName(u"DarkWii_Red_43E")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_43E.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_43E.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_43E.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_43E, 4, 2, 1, 1)

        self.DarkWii_Red_42E = QCheckBox(self.widget)
        self.DarkWii_Red_42E.setObjectName(u"DarkWii_Red_42E")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_42E.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_42E.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_42E.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_42E, 5, 2, 1, 1)

        self.DarkWii_Red_41E = QCheckBox(self.widget)
        self.DarkWii_Red_41E.setObjectName(u"DarkWii_Red_41E")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_41E.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_41E.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_41E.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_41E, 6, 2, 1, 1)

        self.DarkWii_Red_43J = QCheckBox(self.widget)
        self.DarkWii_Red_43J.setObjectName(u"DarkWii_Red_43J")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_43J.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_43J.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_43J.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_43J, 7, 2, 1, 1)

        self.DarkWii_Red_42J = QCheckBox(self.widget)
        self.DarkWii_Red_42J.setObjectName(u"DarkWii_Red_42J")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_42J.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_42J.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_42J.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_42J, 8, 2, 1, 1)

        self.DarkWii_Red_41J = QCheckBox(self.widget)
        self.DarkWii_Red_41J.setObjectName(u"DarkWii_Red_41J")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_41J.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_41J.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_41J.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_41J, 9, 2, 1, 1)

        self.DarkWii_Red_43K = QCheckBox(self.widget)
        self.DarkWii_Red_43K.setObjectName(u"DarkWii_Red_43K")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_43K.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_43K.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_43K.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_43K, 10, 2, 1, 1)

        self.DarkWii_Red_42K = QCheckBox(self.widget)
        self.DarkWii_Red_42K.setObjectName(u"DarkWii_Red_42K")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_42K.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_42K.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_42K.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_42K, 11, 2, 1, 1)

        self.DarkWii_Red_41K = QCheckBox(self.widget)
        self.DarkWii_Red_41K.setObjectName(u"DarkWii_Red_41K")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_41K.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_41K.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_41K.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_41K, 12, 2, 1, 1)

        self.DarkWii_Red_vU = QCheckBox(self.widget)
        self.DarkWii_Red_vU.setObjectName(u"DarkWii_Red_vU")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_vU.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_vU.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_vU.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_vU, 13, 2, 1, 1)

        self.DarkWii_Red_vE = QCheckBox(self.widget)
        self.DarkWii_Red_vE.setObjectName(u"DarkWii_Red_vE")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_vE.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_vE.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_vE.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_vE, 14, 2, 1, 1)

        self.DarkWii_Red_vJ = QCheckBox(self.widget)
        self.DarkWii_Red_vJ.setObjectName(u"DarkWii_Red_vJ")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_vJ.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_vJ.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_vJ.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_vJ, 15, 2, 1, 1)

        self.DarkWii_Green_42U = QCheckBox(self.widget)
        self.DarkWii_Green_42U.setObjectName(u"DarkWii_Green_42U")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_42U.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_42U.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_42U.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_42U, 2, 3, 1, 1)

        self.DarkWii_Green_41U = QCheckBox(self.widget)
        self.DarkWii_Green_41U.setObjectName(u"DarkWii_Green_41U")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_41U.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_41U.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_41U.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_41U, 3, 3, 1, 1)

        self.DarkWii_Green_43E = QCheckBox(self.widget)
        self.DarkWii_Green_43E.setObjectName(u"DarkWii_Green_43E")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_43E.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_43E.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_43E.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_43E, 4, 3, 1, 1)

        self.DarkWii_Green_42E = QCheckBox(self.widget)
        self.DarkWii_Green_42E.setObjectName(u"DarkWii_Green_42E")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_42E.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_42E.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_42E.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_42E, 5, 3, 1, 1)

        self.DarkWii_Green_41E = QCheckBox(self.widget)
        self.DarkWii_Green_41E.setObjectName(u"DarkWii_Green_41E")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_41E.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_41E.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_41E.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_41E, 6, 3, 1, 1)

        self.DarkWii_Green_43J = QCheckBox(self.widget)
        self.DarkWii_Green_43J.setObjectName(u"DarkWii_Green_43J")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_43J.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_43J.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_43J.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_43J, 7, 3, 1, 1)

        self.DarkWii_Green_42J = QCheckBox(self.widget)
        self.DarkWii_Green_42J.setObjectName(u"DarkWii_Green_42J")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_42J.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_42J.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_42J.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_42J, 8, 3, 1, 1)

        self.DarkWii_Green_41J = QCheckBox(self.widget)
        self.DarkWii_Green_41J.setObjectName(u"DarkWii_Green_41J")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_41J.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_41J.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_41J.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_41J, 9, 3, 1, 1)

        self.DarkWii_Green_43K = QCheckBox(self.widget)
        self.DarkWii_Green_43K.setObjectName(u"DarkWii_Green_43K")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_43K.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_43K.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_43K.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_43K, 10, 3, 1, 1)

        self.DarkWii_Green_42K = QCheckBox(self.widget)
        self.DarkWii_Green_42K.setObjectName(u"DarkWii_Green_42K")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_42K.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_42K.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_42K.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_42K, 11, 3, 1, 1)

        self.DarkWii_Green_41K = QCheckBox(self.widget)
        self.DarkWii_Green_41K.setObjectName(u"DarkWii_Green_41K")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_41K.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_41K.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_41K.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_41K, 12, 3, 1, 1)

        self.DarkWii_Green_vU = QCheckBox(self.widget)
        self.DarkWii_Green_vU.setObjectName(u"DarkWii_Green_vU")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_vU.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_vU.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_vU.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_vU, 13, 3, 1, 1)

        self.DarkWii_Green_vE = QCheckBox(self.widget)
        self.DarkWii_Green_vE.setObjectName(u"DarkWii_Green_vE")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_vE.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_vE.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_vE.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_vE, 14, 3, 1, 1)

        self.DarkWii_Green_vJ = QCheckBox(self.widget)
        self.DarkWii_Green_vJ.setObjectName(u"DarkWii_Green_vJ")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_vJ.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_vJ.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_vJ.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_vJ, 15, 3, 1, 1)

        self.DarkWii_Blue_42U = QCheckBox(self.widget)
        self.DarkWii_Blue_42U.setObjectName(u"DarkWii_Blue_42U")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_42U.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_42U.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_42U.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_42U, 2, 4, 1, 1)

        self.DarkWii_Blue_41U = QCheckBox(self.widget)
        self.DarkWii_Blue_41U.setObjectName(u"DarkWii_Blue_41U")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_41U.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_41U.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_41U.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_41U, 3, 4, 1, 1)

        self.DarkWii_Blue_43E = QCheckBox(self.widget)
        self.DarkWii_Blue_43E.setObjectName(u"DarkWii_Blue_43E")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_43E.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_43E.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_43E.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_43E, 4, 4, 1, 1)

        self.DarkWii_Blue_42E = QCheckBox(self.widget)
        self.DarkWii_Blue_42E.setObjectName(u"DarkWii_Blue_42E")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_42E.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_42E.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_42E.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_42E, 5, 4, 1, 1)

        self.DarkWii_Blue_41E = QCheckBox(self.widget)
        self.DarkWii_Blue_41E.setObjectName(u"DarkWii_Blue_41E")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_41E.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_41E.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_41E.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_41E, 6, 4, 1, 1)

        self.DarkWii_Blue_43J = QCheckBox(self.widget)
        self.DarkWii_Blue_43J.setObjectName(u"DarkWii_Blue_43J")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_43J.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_43J.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_43J.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_43J, 7, 4, 1, 1)

        self.DarkWii_Blue_42J = QCheckBox(self.widget)
        self.DarkWii_Blue_42J.setObjectName(u"DarkWii_Blue_42J")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_42J.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_42J.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_42J.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_42J, 8, 4, 1, 1)

        self.DarkWii_Blue_41J = QCheckBox(self.widget)
        self.DarkWii_Blue_41J.setObjectName(u"DarkWii_Blue_41J")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_41J.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_41J.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_41J.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_41J, 9, 4, 1, 1)

        self.DarkWii_Blue_43K = QCheckBox(self.widget)
        self.DarkWii_Blue_43K.setObjectName(u"DarkWii_Blue_43K")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_43K.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_43K.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_43K.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_43K, 10, 4, 1, 1)

        self.DarkWii_Blue_42K = QCheckBox(self.widget)
        self.DarkWii_Blue_42K.setObjectName(u"DarkWii_Blue_42K")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_42K.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_42K.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_42K.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_42K, 11, 4, 1, 1)

        self.DarkWii_Blue_41K = QCheckBox(self.widget)
        self.DarkWii_Blue_41K.setObjectName(u"DarkWii_Blue_41K")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_41K.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_41K.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_41K.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_41K, 12, 4, 1, 1)

        self.DarkWii_Blue_vU = QCheckBox(self.widget)
        self.DarkWii_Blue_vU.setObjectName(u"DarkWii_Blue_vU")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_vU.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_vU.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_vU.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_vU, 13, 4, 1, 1)

        self.DarkWii_Blue_vE = QCheckBox(self.widget)
        self.DarkWii_Blue_vE.setObjectName(u"DarkWii_Blue_vE")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_vE.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_vE.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_vE.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_vE, 14, 4, 1, 1)

        self.DarkWii_Blue_vJ = QCheckBox(self.widget)
        self.DarkWii_Blue_vJ.setObjectName(u"DarkWii_Blue_vJ")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_vJ.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_vJ.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_vJ.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_vJ, 15, 4, 1, 1)

        self.DarkWii_Orange_42U = QCheckBox(self.widget)
        self.DarkWii_Orange_42U.setObjectName(u"DarkWii_Orange_42U")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_42U.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_42U.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_42U.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_42U, 2, 5, 1, 1)

        self.DarkWii_Orange_41U = QCheckBox(self.widget)
        self.DarkWii_Orange_41U.setObjectName(u"DarkWii_Orange_41U")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_41U.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_41U.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_41U.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_41U, 3, 5, 1, 1)

        self.DarkWii_Orange_43E = QCheckBox(self.widget)
        self.DarkWii_Orange_43E.setObjectName(u"DarkWii_Orange_43E")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_43E.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_43E.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_43E.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_43E, 4, 5, 1, 1)

        self.DarkWii_Orange_42E = QCheckBox(self.widget)
        self.DarkWii_Orange_42E.setObjectName(u"DarkWii_Orange_42E")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_42E.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_42E.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_42E.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_42E, 5, 5, 1, 1)

        self.DarkWii_Orange_41E = QCheckBox(self.widget)
        self.DarkWii_Orange_41E.setObjectName(u"DarkWii_Orange_41E")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_41E.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_41E.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_41E.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_41E, 6, 5, 1, 1)

        self.DarkWii_Orange_43J = QCheckBox(self.widget)
        self.DarkWii_Orange_43J.setObjectName(u"DarkWii_Orange_43J")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_43J.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_43J.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_43J.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_43J, 7, 5, 1, 1)

        self.DarkWii_Orange_42J = QCheckBox(self.widget)
        self.DarkWii_Orange_42J.setObjectName(u"DarkWii_Orange_42J")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_42J.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_42J.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_42J.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_42J, 8, 5, 1, 1)

        self.DarkWii_Orange_41J = QCheckBox(self.widget)
        self.DarkWii_Orange_41J.setObjectName(u"DarkWii_Orange_41J")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_41J.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_41J.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_41J.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_41J, 9, 5, 1, 1)

        self.DarkWii_Orange_43K = QCheckBox(self.widget)
        self.DarkWii_Orange_43K.setObjectName(u"DarkWii_Orange_43K")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_43K.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_43K.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_43K.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_43K, 10, 5, 1, 1)

        self.DarkWii_Orange_42K = QCheckBox(self.widget)
        self.DarkWii_Orange_42K.setObjectName(u"DarkWii_Orange_42K")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_42K.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_42K.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_42K.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_42K, 11, 5, 1, 1)

        self.DarkWii_Orange_41K = QCheckBox(self.widget)
        self.DarkWii_Orange_41K.setObjectName(u"DarkWii_Orange_41K")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_41K.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_41K.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_41K.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_41K, 12, 5, 1, 1)

        self.DarkWii_Orange_vU = QCheckBox(self.widget)
        self.DarkWii_Orange_vU.setObjectName(u"DarkWii_Orange_vU")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_vU.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_vU.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_vU.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_vU, 13, 5, 1, 1)

        self.DarkWii_Orange_vE = QCheckBox(self.widget)
        self.DarkWii_Orange_vE.setObjectName(u"DarkWii_Orange_vE")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_vE.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_vE.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_vE.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_vE, 14, 5, 1, 1)

        self.DarkWii_Orange_vJ = QCheckBox(self.widget)
        self.DarkWii_Orange_vJ.setObjectName(u"DarkWii_Orange_vJ")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_vJ.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_vJ.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_vJ.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_vJ, 15, 5, 1, 1)

        self.DarkWii_Red_42U_W = QCheckBox(self.widget)
        self.DarkWii_Red_42U_W.setObjectName(u"DarkWii_Red_42U_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_42U_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_42U_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_42U_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_42U_W, 2, 6, 1, 1)

        self.DarkWii_Red_41U_W = QCheckBox(self.widget)
        self.DarkWii_Red_41U_W.setObjectName(u"DarkWii_Red_41U_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_41U_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_41U_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_41U_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_41U_W, 3, 6, 1, 1)

        self.DarkWii_Red_43E_W = QCheckBox(self.widget)
        self.DarkWii_Red_43E_W.setObjectName(u"DarkWii_Red_43E_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_43E_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_43E_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_43E_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_43E_W, 4, 6, 1, 1)

        self.DarkWii_Red_42E_W = QCheckBox(self.widget)
        self.DarkWii_Red_42E_W.setObjectName(u"DarkWii_Red_42E_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_42E_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_42E_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_42E_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_42E_W, 5, 6, 1, 1)

        self.DarkWii_Red_41E_W = QCheckBox(self.widget)
        self.DarkWii_Red_41E_W.setObjectName(u"DarkWii_Red_41E_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_41E_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_41E_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_41E_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_41E_W, 6, 6, 1, 1)

        self.DarkWii_Red_43J_W = QCheckBox(self.widget)
        self.DarkWii_Red_43J_W.setObjectName(u"DarkWii_Red_43J_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_43J_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_43J_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_43J_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_43J_W, 7, 6, 1, 1)

        self.DarkWii_Red_42J_W = QCheckBox(self.widget)
        self.DarkWii_Red_42J_W.setObjectName(u"DarkWii_Red_42J_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_42J_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_42J_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_42J_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_42J_W, 8, 6, 1, 1)

        self.DarkWii_Red_41J_W = QCheckBox(self.widget)
        self.DarkWii_Red_41J_W.setObjectName(u"DarkWii_Red_41J_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_41J_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_41J_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_41J_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_41J_W, 9, 6, 1, 1)

        self.DarkWii_Red_43K_W = QCheckBox(self.widget)
        self.DarkWii_Red_43K_W.setObjectName(u"DarkWii_Red_43K_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_43K_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_43K_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_43K_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_43K_W, 10, 6, 1, 1)

        self.DarkWii_Red_42K_W = QCheckBox(self.widget)
        self.DarkWii_Red_42K_W.setObjectName(u"DarkWii_Red_42K_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_42K_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_42K_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_42K_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_42K_W, 11, 6, 1, 1)

        self.DarkWii_Red_41K_W = QCheckBox(self.widget)
        self.DarkWii_Red_41K_W.setObjectName(u"DarkWii_Red_41K_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Red_41K_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Red_41K_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Red_41K_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Red_41K_W, 12, 6, 1, 1)

        self.DarkWii_Green_42U_W = QCheckBox(self.widget)
        self.DarkWii_Green_42U_W.setObjectName(u"DarkWii_Green_42U_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_42U_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_42U_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_42U_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_42U_W, 2, 7, 1, 1)

        self.DarkWii_Green_41U_W = QCheckBox(self.widget)
        self.DarkWii_Green_41U_W.setObjectName(u"DarkWii_Green_41U_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_41U_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_41U_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_41U_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_41U_W, 3, 7, 1, 1)

        self.DarkWii_Green_43E_W = QCheckBox(self.widget)
        self.DarkWii_Green_43E_W.setObjectName(u"DarkWii_Green_43E_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_43E_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_43E_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_43E_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_43E_W, 4, 7, 1, 1)

        self.DarkWii_Green_42E_W = QCheckBox(self.widget)
        self.DarkWii_Green_42E_W.setObjectName(u"DarkWii_Green_42E_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_42E_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_42E_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_42E_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_42E_W, 5, 7, 1, 1)

        self.DarkWii_Green_41E_W = QCheckBox(self.widget)
        self.DarkWii_Green_41E_W.setObjectName(u"DarkWii_Green_41E_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_41E_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_41E_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_41E_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_41E_W, 6, 7, 1, 1)

        self.DarkWii_Green_43J_W = QCheckBox(self.widget)
        self.DarkWii_Green_43J_W.setObjectName(u"DarkWii_Green_43J_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_43J_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_43J_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_43J_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_43J_W, 7, 7, 1, 1)

        self.DarkWii_Green_42J_W = QCheckBox(self.widget)
        self.DarkWii_Green_42J_W.setObjectName(u"DarkWii_Green_42J_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_42J_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_42J_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_42J_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_42J_W, 8, 7, 1, 1)

        self.DarkWii_Green_41J_W = QCheckBox(self.widget)
        self.DarkWii_Green_41J_W.setObjectName(u"DarkWii_Green_41J_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_41J_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_41J_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_41J_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_41J_W, 9, 7, 1, 1)

        self.DarkWii_Green_43K_W = QCheckBox(self.widget)
        self.DarkWii_Green_43K_W.setObjectName(u"DarkWii_Green_43K_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_43K_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_43K_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_43K_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_43K_W, 10, 7, 1, 1)

        self.DarkWii_Green_42K_W = QCheckBox(self.widget)
        self.DarkWii_Green_42K_W.setObjectName(u"DarkWii_Green_42K_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_42K_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_42K_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_42K_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_42K_W, 11, 7, 1, 1)

        self.DarkWii_Green_41K_W = QCheckBox(self.widget)
        self.DarkWii_Green_41K_W.setObjectName(u"DarkWii_Green_41K_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Green_41K_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Green_41K_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Green_41K_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Green_41K_W, 12, 7, 1, 1)

        self.DarkWii_Blue_42U_W = QCheckBox(self.widget)
        self.DarkWii_Blue_42U_W.setObjectName(u"DarkWii_Blue_42U_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_42U_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_42U_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_42U_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_42U_W, 2, 8, 1, 1)

        self.DarkWii_Blue_41U_W = QCheckBox(self.widget)
        self.DarkWii_Blue_41U_W.setObjectName(u"DarkWii_Blue_41U_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_41U_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_41U_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_41U_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_41U_W, 3, 8, 1, 1)

        self.DarkWii_Blue_43E_W = QCheckBox(self.widget)
        self.DarkWii_Blue_43E_W.setObjectName(u"DarkWii_Blue_43E_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_43E_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_43E_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_43E_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_43E_W, 4, 8, 1, 1)

        self.DarkWii_Blue_42E_W = QCheckBox(self.widget)
        self.DarkWii_Blue_42E_W.setObjectName(u"DarkWii_Blue_42E_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_42E_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_42E_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_42E_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_42E_W, 5, 8, 1, 1)

        self.DarkWii_Blue_41E_W = QCheckBox(self.widget)
        self.DarkWii_Blue_41E_W.setObjectName(u"DarkWii_Blue_41E_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_41E_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_41E_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_41E_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_41E_W, 6, 8, 1, 1)

        self.DarkWii_Blue_43J_W = QCheckBox(self.widget)
        self.DarkWii_Blue_43J_W.setObjectName(u"DarkWii_Blue_43J_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_43J_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_43J_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_43J_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_43J_W, 7, 8, 1, 1)

        self.DarkWii_Blue_42J_W = QCheckBox(self.widget)
        self.DarkWii_Blue_42J_W.setObjectName(u"DarkWii_Blue_42J_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_42J_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_42J_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_42J_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_42J_W, 8, 8, 1, 1)

        self.DarkWii_Blue_41J_W = QCheckBox(self.widget)
        self.DarkWii_Blue_41J_W.setObjectName(u"DarkWii_Blue_41J_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_41J_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_41J_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_41J_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_41J_W, 9, 8, 1, 1)

        self.DarkWii_Blue_43K_W = QCheckBox(self.widget)
        self.DarkWii_Blue_43K_W.setObjectName(u"DarkWii_Blue_43K_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_43K_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_43K_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_43K_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_43K_W, 10, 8, 1, 1)

        self.DarkWii_Blue_42K_W = QCheckBox(self.widget)
        self.DarkWii_Blue_42K_W.setObjectName(u"DarkWii_Blue_42K_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_42K_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_42K_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_42K_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_42K_W, 11, 8, 1, 1)

        self.DarkWii_Blue_41K_W = QCheckBox(self.widget)
        self.DarkWii_Blue_41K_W.setObjectName(u"DarkWii_Blue_41K_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Blue_41K_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Blue_41K_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Blue_41K_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Blue_41K_W, 12, 8, 1, 1)

        self.DarkWii_Orange_42U_W = QCheckBox(self.widget)
        self.DarkWii_Orange_42U_W.setObjectName(u"DarkWii_Orange_42U_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_42U_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_42U_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_42U_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_42U_W, 2, 9, 1, 1)

        self.DarkWii_Orange_41U_W = QCheckBox(self.widget)
        self.DarkWii_Orange_41U_W.setObjectName(u"DarkWii_Orange_41U_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_41U_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_41U_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_41U_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_41U_W, 3, 9, 1, 1)

        self.DarkWii_Orange_43E_W = QCheckBox(self.widget)
        self.DarkWii_Orange_43E_W.setObjectName(u"DarkWii_Orange_43E_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_43E_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_43E_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_43E_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_43E_W, 4, 9, 1, 1)

        self.DarkWii_Orange_42E_W = QCheckBox(self.widget)
        self.DarkWii_Orange_42E_W.setObjectName(u"DarkWii_Orange_42E_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_42E_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_42E_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_42E_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_42E_W, 5, 9, 1, 1)

        self.DarkWii_Orange_41E_W = QCheckBox(self.widget)
        self.DarkWii_Orange_41E_W.setObjectName(u"DarkWii_Orange_41E_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_41E_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_41E_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_41E_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_41E_W, 6, 9, 1, 1)

        self.DarkWii_Orange_43J_W = QCheckBox(self.widget)
        self.DarkWii_Orange_43J_W.setObjectName(u"DarkWii_Orange_43J_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_43J_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_43J_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_43J_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_43J_W, 7, 9, 1, 1)

        self.DarkWii_Orange_42J_W = QCheckBox(self.widget)
        self.DarkWii_Orange_42J_W.setObjectName(u"DarkWii_Orange_42J_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_42J_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_42J_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_42J_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_42J_W, 8, 9, 1, 1)

        self.DarkWii_Orange_41J_W = QCheckBox(self.widget)
        self.DarkWii_Orange_41J_W.setObjectName(u"DarkWii_Orange_41J_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_41J_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_41J_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_41J_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_41J_W, 9, 9, 1, 1)

        self.DarkWii_Orange_43K_W = QCheckBox(self.widget)
        self.DarkWii_Orange_43K_W.setObjectName(u"DarkWii_Orange_43K_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_43K_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_43K_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_43K_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_43K_W, 10, 9, 1, 1)

        self.DarkWii_Orange_42K_W = QCheckBox(self.widget)
        self.DarkWii_Orange_42K_W.setObjectName(u"DarkWii_Orange_42K_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_42K_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_42K_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_42K_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_42K_W, 11, 9, 1, 1)

        self.DarkWii_Orange_41K_W = QCheckBox(self.widget)
        self.DarkWii_Orange_41K_W.setObjectName(u"DarkWii_Orange_41K_W")
        sizePolicy1.setHeightForWidth(self.DarkWii_Orange_41K_W.sizePolicy().hasHeightForWidth())
        self.DarkWii_Orange_41K_W.setSizePolicy(sizePolicy1)
        self.DarkWii_Orange_41K_W.setStyleSheet(u"")

        self.layout.addWidget(self.DarkWii_Orange_41K_W, 12, 9, 1, 1)

        self.layout.setColumnMinimumWidth(0, 60)
        self.layout.setColumnMinimumWidth(1, 60)
        self.layout.setColumnMinimumWidth(2, 60)
        self.layout.setColumnMinimumWidth(3, 60)
        self.layout.setColumnMinimumWidth(4, 60)
        self.layout.setColumnMinimumWidth(5, 60)
        self.layout.setColumnMinimumWidth(6, 60)
        self.layout.setColumnMinimumWidth(7, 60)
        self.layout.setColumnMinimumWidth(8, 60)
        self.layout.setColumnMinimumWidth(9, 60)
        QWidget.setTabOrder(self.youtube, self.a)
        QWidget.setTabOrder(self.a, self.b)
        QWidget.setTabOrder(self.b, self.c)
        QWidget.setTabOrder(self.c, self.d)
        QWidget.setTabOrder(self.d, self.e)
        QWidget.setTabOrder(self.e, self.f)
        QWidget.setTabOrder(self.f, self.g)
        QWidget.setTabOrder(self.g, self.h)
        QWidget.setTabOrder(self.h, self.i)
        QWidget.setTabOrder(self.i, self.s43U)
        QWidget.setTabOrder(self.s43U, self.s42U)
        QWidget.setTabOrder(self.s42U, self.s41U)
        QWidget.setTabOrder(self.s41U, self.s43E)
        QWidget.setTabOrder(self.s43E, self.s42E)
        QWidget.setTabOrder(self.s42E, self.s41E)
        QWidget.setTabOrder(self.s41E, self.s43J)
        QWidget.setTabOrder(self.s43J, self.s42J)
        QWidget.setTabOrder(self.s42J, self.s41J)
        QWidget.setTabOrder(self.s41J, self.s43K)
        QWidget.setTabOrder(self.s43K, self.s42K)
        QWidget.setTabOrder(self.s42K, self.s41K)
        QWidget.setTabOrder(self.s41K, self.svU)
        QWidget.setTabOrder(self.svU, self.svE)
        QWidget.setTabOrder(self.svE, self.svJ)
        QWidget.setTabOrder(self.svJ, self.O_43U)
        QWidget.setTabOrder(self.O_43U, self.O_42U)
        QWidget.setTabOrder(self.O_42U, self.O_41U)
        QWidget.setTabOrder(self.O_41U, self.O_43E)
        QWidget.setTabOrder(self.O_43E, self.O_42E)
        QWidget.setTabOrder(self.O_42E, self.O_41E)
        QWidget.setTabOrder(self.O_41E, self.O_43J)
        QWidget.setTabOrder(self.O_43J, self.O_42J)
        QWidget.setTabOrder(self.O_42J, self.O_41J)
        QWidget.setTabOrder(self.O_41J, self.O_43K)
        QWidget.setTabOrder(self.O_43K, self.O_42K)
        QWidget.setTabOrder(self.O_42K, self.O_41K)
        QWidget.setTabOrder(self.O_41K, self.O_vU)
        QWidget.setTabOrder(self.O_vU, self.O_vE)
        QWidget.setTabOrder(self.O_vE, self.O_vJ)
        QWidget.setTabOrder(self.O_vJ, self.DarkWii_Red_43U)
        QWidget.setTabOrder(self.DarkWii_Red_43U, self.DarkWii_Red_42U)
        QWidget.setTabOrder(self.DarkWii_Red_42U, self.DarkWii_Red_41U)
        QWidget.setTabOrder(self.DarkWii_Red_41U, self.DarkWii_Red_43E)
        QWidget.setTabOrder(self.DarkWii_Red_43E, self.DarkWii_Red_42E)
        QWidget.setTabOrder(self.DarkWii_Red_42E, self.DarkWii_Red_41E)
        QWidget.setTabOrder(self.DarkWii_Red_41E, self.DarkWii_Red_43J)
        QWidget.setTabOrder(self.DarkWii_Red_43J, self.DarkWii_Red_42J)
        QWidget.setTabOrder(self.DarkWii_Red_42J, self.DarkWii_Red_41J)
        QWidget.setTabOrder(self.DarkWii_Red_41J, self.DarkWii_Red_43K)
        QWidget.setTabOrder(self.DarkWii_Red_43K, self.DarkWii_Red_42K)
        QWidget.setTabOrder(self.DarkWii_Red_42K, self.DarkWii_Red_41K)
        QWidget.setTabOrder(self.DarkWii_Red_41K, self.DarkWii_Red_vU)
        QWidget.setTabOrder(self.DarkWii_Red_vU, self.DarkWii_Red_vE)
        QWidget.setTabOrder(self.DarkWii_Red_vE, self.DarkWii_Red_vJ)
        QWidget.setTabOrder(self.DarkWii_Red_vJ, self.DarkWii_Green_43U)
        QWidget.setTabOrder(self.DarkWii_Green_43U, self.DarkWii_Green_42U)
        QWidget.setTabOrder(self.DarkWii_Green_42U, self.DarkWii_Green_41U)
        QWidget.setTabOrder(self.DarkWii_Green_41U, self.DarkWii_Green_43E)
        QWidget.setTabOrder(self.DarkWii_Green_43E, self.DarkWii_Green_42E)
        QWidget.setTabOrder(self.DarkWii_Green_42E, self.DarkWii_Green_41E)
        QWidget.setTabOrder(self.DarkWii_Green_41E, self.DarkWii_Green_43J)
        QWidget.setTabOrder(self.DarkWii_Green_43J, self.DarkWii_Green_42J)
        QWidget.setTabOrder(self.DarkWii_Green_42J, self.DarkWii_Green_41J)
        QWidget.setTabOrder(self.DarkWii_Green_41J, self.DarkWii_Green_43K)
        QWidget.setTabOrder(self.DarkWii_Green_43K, self.DarkWii_Green_42K)
        QWidget.setTabOrder(self.DarkWii_Green_42K, self.DarkWii_Green_41K)
        QWidget.setTabOrder(self.DarkWii_Green_41K, self.DarkWii_Green_vU)
        QWidget.setTabOrder(self.DarkWii_Green_vU, self.DarkWii_Green_vE)
        QWidget.setTabOrder(self.DarkWii_Green_vE, self.DarkWii_Green_vJ)
        QWidget.setTabOrder(self.DarkWii_Green_vJ, self.DarkWii_Blue_43U)
        QWidget.setTabOrder(self.DarkWii_Blue_43U, self.DarkWii_Blue_42U)
        QWidget.setTabOrder(self.DarkWii_Blue_42U, self.DarkWii_Blue_41U)
        QWidget.setTabOrder(self.DarkWii_Blue_41U, self.DarkWii_Blue_43E)
        QWidget.setTabOrder(self.DarkWii_Blue_43E, self.DarkWii_Blue_42E)
        QWidget.setTabOrder(self.DarkWii_Blue_42E, self.DarkWii_Blue_41E)
        QWidget.setTabOrder(self.DarkWii_Blue_41E, self.DarkWii_Blue_43J)
        QWidget.setTabOrder(self.DarkWii_Blue_43J, self.DarkWii_Blue_42J)
        QWidget.setTabOrder(self.DarkWii_Blue_42J, self.DarkWii_Blue_41J)
        QWidget.setTabOrder(self.DarkWii_Blue_41J, self.DarkWii_Blue_43K)
        QWidget.setTabOrder(self.DarkWii_Blue_43K, self.DarkWii_Blue_42K)
        QWidget.setTabOrder(self.DarkWii_Blue_42K, self.DarkWii_Blue_41K)
        QWidget.setTabOrder(self.DarkWii_Blue_41K, self.DarkWii_Blue_vU)
        QWidget.setTabOrder(self.DarkWii_Blue_vU, self.DarkWii_Blue_vE)
        QWidget.setTabOrder(self.DarkWii_Blue_vE, self.DarkWii_Blue_vJ)
        QWidget.setTabOrder(self.DarkWii_Blue_vJ, self.DarkWii_Orange_43U)
        QWidget.setTabOrder(self.DarkWii_Orange_43U, self.DarkWii_Orange_42U)
        QWidget.setTabOrder(self.DarkWii_Orange_42U, self.DarkWii_Orange_41U)
        QWidget.setTabOrder(self.DarkWii_Orange_41U, self.DarkWii_Orange_43E)
        QWidget.setTabOrder(self.DarkWii_Orange_43E, self.DarkWii_Orange_42E)
        QWidget.setTabOrder(self.DarkWii_Orange_42E, self.DarkWii_Orange_41E)
        QWidget.setTabOrder(self.DarkWii_Orange_41E, self.DarkWii_Orange_43J)
        QWidget.setTabOrder(self.DarkWii_Orange_43J, self.DarkWii_Orange_42J)
        QWidget.setTabOrder(self.DarkWii_Orange_42J, self.DarkWii_Orange_41J)
        QWidget.setTabOrder(self.DarkWii_Orange_41J, self.DarkWii_Orange_43K)
        QWidget.setTabOrder(self.DarkWii_Orange_43K, self.DarkWii_Orange_42K)
        QWidget.setTabOrder(self.DarkWii_Orange_42K, self.DarkWii_Orange_41K)
        QWidget.setTabOrder(self.DarkWii_Orange_41K, self.DarkWii_Orange_vU)
        QWidget.setTabOrder(self.DarkWii_Orange_vU, self.DarkWii_Orange_vE)
        QWidget.setTabOrder(self.DarkWii_Orange_vE, self.DarkWii_Orange_vJ)
        QWidget.setTabOrder(self.DarkWii_Orange_vJ, self.DarkWii_Red_43U_W)
        QWidget.setTabOrder(self.DarkWii_Red_43U_W, self.DarkWii_Red_42U_W)
        QWidget.setTabOrder(self.DarkWii_Red_42U_W, self.DarkWii_Red_41U_W)
        QWidget.setTabOrder(self.DarkWii_Red_41U_W, self.DarkWii_Red_43E_W)
        QWidget.setTabOrder(self.DarkWii_Red_43E_W, self.DarkWii_Red_42E_W)
        QWidget.setTabOrder(self.DarkWii_Red_42E_W, self.DarkWii_Red_41E_W)
        QWidget.setTabOrder(self.DarkWii_Red_41E_W, self.DarkWii_Red_43J_W)
        QWidget.setTabOrder(self.DarkWii_Red_43J_W, self.DarkWii_Red_42J_W)
        QWidget.setTabOrder(self.DarkWii_Red_42J_W, self.DarkWii_Red_41J_W)
        QWidget.setTabOrder(self.DarkWii_Red_41J_W, self.DarkWii_Red_43K_W)
        QWidget.setTabOrder(self.DarkWii_Red_43K_W, self.DarkWii_Red_42K_W)
        QWidget.setTabOrder(self.DarkWii_Red_42K_W, self.DarkWii_Red_41K_W)
        QWidget.setTabOrder(self.DarkWii_Red_41K_W, self.DarkWii_Green_43U_W)
        QWidget.setTabOrder(self.DarkWii_Green_43U_W, self.DarkWii_Green_42U_W)
        QWidget.setTabOrder(self.DarkWii_Green_42U_W, self.DarkWii_Green_41U_W)
        QWidget.setTabOrder(self.DarkWii_Green_41U_W, self.DarkWii_Green_43E_W)
        QWidget.setTabOrder(self.DarkWii_Green_43E_W, self.DarkWii_Green_42E_W)
        QWidget.setTabOrder(self.DarkWii_Green_42E_W, self.DarkWii_Green_41E_W)
        QWidget.setTabOrder(self.DarkWii_Green_41E_W, self.DarkWii_Green_43J_W)
        QWidget.setTabOrder(self.DarkWii_Green_43J_W, self.DarkWii_Green_42J_W)
        QWidget.setTabOrder(self.DarkWii_Green_42J_W, self.DarkWii_Green_41J_W)
        QWidget.setTabOrder(self.DarkWii_Green_41J_W, self.DarkWii_Green_43K_W)
        QWidget.setTabOrder(self.DarkWii_Green_43K_W, self.DarkWii_Green_42K_W)
        QWidget.setTabOrder(self.DarkWii_Green_42K_W, self.DarkWii_Green_41K_W)
        QWidget.setTabOrder(self.DarkWii_Green_41K_W, self.DarkWii_Blue_43U_W)
        QWidget.setTabOrder(self.DarkWii_Blue_43U_W, self.DarkWii_Blue_42U_W)
        QWidget.setTabOrder(self.DarkWii_Blue_42U_W, self.DarkWii_Blue_41U_W)
        QWidget.setTabOrder(self.DarkWii_Blue_41U_W, self.DarkWii_Blue_43E_W)
        QWidget.setTabOrder(self.DarkWii_Blue_43E_W, self.DarkWii_Blue_42E_W)
        QWidget.setTabOrder(self.DarkWii_Blue_42E_W, self.DarkWii_Blue_41E_W)
        QWidget.setTabOrder(self.DarkWii_Blue_41E_W, self.DarkWii_Blue_43J_W)
        QWidget.setTabOrder(self.DarkWii_Blue_43J_W, self.DarkWii_Blue_42J_W)
        QWidget.setTabOrder(self.DarkWii_Blue_42J_W, self.DarkWii_Blue_41J_W)
        QWidget.setTabOrder(self.DarkWii_Blue_41J_W, self.DarkWii_Blue_43K_W)
        QWidget.setTabOrder(self.DarkWii_Blue_43K_W, self.DarkWii_Blue_42K_W)
        QWidget.setTabOrder(self.DarkWii_Blue_42K_W, self.DarkWii_Blue_41K_W)
        QWidget.setTabOrder(self.DarkWii_Blue_41K_W, self.DarkWii_Orange_43U_W)
        QWidget.setTabOrder(self.DarkWii_Orange_43U_W, self.DarkWii_Orange_42U_W)
        QWidget.setTabOrder(self.DarkWii_Orange_42U_W, self.DarkWii_Orange_41U_W)
        QWidget.setTabOrder(self.DarkWii_Orange_41U_W, self.DarkWii_Orange_43E_W)
        QWidget.setTabOrder(self.DarkWii_Orange_43E_W, self.DarkWii_Orange_42E_W)
        QWidget.setTabOrder(self.DarkWii_Orange_42E_W, self.DarkWii_Orange_41E_W)
        QWidget.setTabOrder(self.DarkWii_Orange_41E_W, self.DarkWii_Orange_43J_W)
        QWidget.setTabOrder(self.DarkWii_Orange_43J_W, self.DarkWii_Orange_42J_W)
        QWidget.setTabOrder(self.DarkWii_Orange_42J_W, self.DarkWii_Orange_41J_W)
        QWidget.setTabOrder(self.DarkWii_Orange_41J_W, self.DarkWii_Orange_43K_W)
        QWidget.setTabOrder(self.DarkWii_Orange_43K_W, self.DarkWii_Orange_42K_W)
        QWidget.setTabOrder(self.DarkWii_Orange_42K_W, self.DarkWii_Orange_41K_W)

        self.retranslateUi(ThemeGrid)

        QMetaObject.connectSlotsByName(ThemeGrid)
    # setupUi

    def retranslateUi(self, ThemeGrid):
        self.s43E.setText(QCoreApplication.translate("ThemeGrid", u"4.3E", None))
        self.s43U.setText(QCoreApplication.translate("ThemeGrid", u"4.3U", None))
        self.c.setText(QCoreApplication.translate("ThemeGrid", u"Green\n"
"CSM", None))
        self.s42J.setText(QCoreApplication.translate("ThemeGrid", u"4.2J", None))
        self.g.setText(QCoreApplication.translate("ThemeGrid", u"Green\n"
"WAD", None))
        self.s41J.setText(QCoreApplication.translate("ThemeGrid", u"4.1J", None))
        self.e.setText(QCoreApplication.translate("ThemeGrid", u"Orange\n"
"CSM", None))
        self.d.setText(QCoreApplication.translate("ThemeGrid", u"Blue\n"
"CSM", None))
        self.s41K.setText(QCoreApplication.translate("ThemeGrid", u"4.1K", None))
        self.svU.setText(QCoreApplication.translate("ThemeGrid", u"vWii U", None))
#if QT_CONFIG(tooltip)
        self.youtube.setToolTip(QCoreApplication.translate("ThemeGrid", u"To restore the original Wii theme, install the 000000XX.app file for your System Menu version using MyMenuifyMod or csm-installer.", None))
#endif // QT_CONFIG(tooltip)
        self.youtube.setText(QCoreApplication.translate("ThemeGrid", u"Youtube\n"
"Preview", None))
        self.s42K.setText(QCoreApplication.translate("ThemeGrid", u"4.2K", None))
        self.s43J.setText(QCoreApplication.translate("ThemeGrid", u"4.3J", None))
        self.b.setText(QCoreApplication.translate("ThemeGrid", u"Red\n"
"CSM", None))
        self.s41U.setText(QCoreApplication.translate("ThemeGrid", u"4.1U", None))
        self.f.setText(QCoreApplication.translate("ThemeGrid", u"Red\n"
"WAD", None))
        self.s41E.setText(QCoreApplication.translate("ThemeGrid", u"4.1E", None))
        self.i.setText(QCoreApplication.translate("ThemeGrid", u"Orange\n"
"WAD", None))
        self.s42U.setText(QCoreApplication.translate("ThemeGrid", u"4.2U", None))
        self.s43K.setText(QCoreApplication.translate("ThemeGrid", u"4.3K", None))
        self.svJ.setText(QCoreApplication.translate("ThemeGrid", u"vWii J", None))
        self.h.setText(QCoreApplication.translate("ThemeGrid", u"Blue\n"
"WAD", None))
        self.a.setText(QCoreApplication.translate("ThemeGrid", u"Original\n"
"APP", None))
        self.s42E.setText(QCoreApplication.translate("ThemeGrid", u"4.2E", None))
        self.svE.setText(QCoreApplication.translate("ThemeGrid", u"vWii E", None))
        pass
    # retranslateUi

