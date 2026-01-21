# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextBrowser, QWidget)

from d2xCheckGrid import d2xCheckGrid
from waninCheckGrid import waninCheckGrid

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"Downloads/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setIconSize(QSize(32, 32))
        mainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 800, 720))
        self.tabWidget.setDocumentMode(True)
        self.nus = QWidget()
        self.nus.setObjectName(u"nus")
        self.gridLayoutWidget = QWidget(self.nus)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 800, 681))
        self.nusLayout = QGridLayout(self.gridLayoutWidget)
        self.nusLayout.setSpacing(5)
        self.nusLayout.setObjectName(u"nusLayout")
        self.nusLayout.setContentsMargins(0, 0, 0, 0)
        self.channels = QGroupBox(self.gridLayoutWidget)
        self.channels.setObjectName(u"channels")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.channels.sizePolicy().hasHeightForWidth())
        self.channels.setSizePolicy(sizePolicy1)
        self.channels.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.channelList = QListWidget(self.channels)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        QListWidgetItem(self.channelList)
        self.channelList.setObjectName(u"channelList")
        self.channelList.setGeometry(QRect(0, 21, 262, 316))
        sizePolicy.setHeightForWidth(self.channelList.sizePolicy().hasHeightForWidth())
        self.channelList.setSizePolicy(sizePolicy)
        self.channelList.setAlternatingRowColors(True)
        self.channelList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.channelList.setUniformItemSizes(False)

        self.nusLayout.addWidget(self.channels, 1, 1, 1, 1)

        self.contents = QGroupBox(self.gridLayoutWidget)
        self.contents.setObjectName(u"contents")
        sizePolicy1.setHeightForWidth(self.contents.sizePolicy().hasHeightForWidth())
        self.contents.setSizePolicy(sizePolicy1)
        self.contents.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.contentList = QListWidget(self.contents)
        QListWidgetItem(self.contentList)
        QListWidgetItem(self.contentList)
        QListWidgetItem(self.contentList)
        QListWidgetItem(self.contentList)
        self.contentList.setObjectName(u"contentList")
        self.contentList.setGeometry(QRect(0, 21, 263, 316))
        sizePolicy.setHeightForWidth(self.contentList.sizePolicy().hasHeightForWidth())
        self.contentList.setSizePolicy(sizePolicy)
        self.contentList.setAlternatingRowColors(True)
        self.contentList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.contentList.setUniformItemSizes(False)

        self.nusLayout.addWidget(self.contents, 1, 0, 1, 1)

        self.realsigned = QGroupBox(self.gridLayoutWidget)
        self.realsigned.setObjectName(u"realsigned")
        sizePolicy1.setHeightForWidth(self.realsigned.sizePolicy().hasHeightForWidth())
        self.realsigned.setSizePolicy(sizePolicy1)
        self.realsigned.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.realsignedList = QListWidget(self.realsigned)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        QListWidgetItem(self.realsignedList)
        self.realsignedList.setObjectName(u"realsignedList")
        self.realsignedList.setGeometry(QRect(0, 21, 262, 316))
        sizePolicy.setHeightForWidth(self.realsignedList.sizePolicy().hasHeightForWidth())
        self.realsignedList.setSizePolicy(sizePolicy)
        self.realsignedList.setAlternatingRowColors(True)
        self.realsignedList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.realsignedList.setUniformItemSizes(False)

        self.nusLayout.addWidget(self.realsigned, 0, 1, 1, 1)

        self.other = QGroupBox(self.gridLayoutWidget)
        self.other.setObjectName(u"other")
        sizePolicy1.setHeightForWidth(self.other.sizePolicy().hasHeightForWidth())
        self.other.setSizePolicy(sizePolicy1)
        self.other.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.otherList = QListWidget(self.other)
        QListWidgetItem(self.otherList)
        QListWidgetItem(self.otherList)
        QListWidgetItem(self.otherList)
        QListWidgetItem(self.otherList)
        QListWidgetItem(self.otherList)
        QListWidgetItem(self.otherList)
        QListWidgetItem(self.otherList)
        QListWidgetItem(self.otherList)
        QListWidgetItem(self.otherList)
        QListWidgetItem(self.otherList)
        QListWidgetItem(self.otherList)
        QListWidgetItem(self.otherList)
        self.otherList.setObjectName(u"otherList")
        self.otherList.setGeometry(QRect(0, 21, 263, 316))
        sizePolicy.setHeightForWidth(self.otherList.sizePolicy().hasHeightForWidth())
        self.otherList.setSizePolicy(sizePolicy)
        self.otherList.setAlternatingRowColors(True)
        self.otherList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.otherList.setUniformItemSizes(False)

        self.nusLayout.addWidget(self.other, 1, 2, 1, 1)

        self.fakesigned = QGroupBox(self.gridLayoutWidget)
        self.fakesigned.setObjectName(u"fakesigned")
        sizePolicy1.setHeightForWidth(self.fakesigned.sizePolicy().hasHeightForWidth())
        self.fakesigned.setSizePolicy(sizePolicy1)
        self.fakesigned.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fakesignedList = QListWidget(self.fakesigned)
        QListWidgetItem(self.fakesignedList)
        QListWidgetItem(self.fakesignedList)
        QListWidgetItem(self.fakesignedList)
        QListWidgetItem(self.fakesignedList)
        QListWidgetItem(self.fakesignedList)
        QListWidgetItem(self.fakesignedList)
        QListWidgetItem(self.fakesignedList)
        QListWidgetItem(self.fakesignedList)
        QListWidgetItem(self.fakesignedList)
        QListWidgetItem(self.fakesignedList)
        QListWidgetItem(self.fakesignedList)
        QListWidgetItem(self.fakesignedList)
        self.fakesignedList.setObjectName(u"fakesignedList")
        self.fakesignedList.setGeometry(QRect(0, 21, 263, 316))
        sizePolicy.setHeightForWidth(self.fakesignedList.sizePolicy().hasHeightForWidth())
        self.fakesignedList.setSizePolicy(sizePolicy)
        self.fakesignedList.setAlternatingRowColors(True)
        self.fakesignedList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.fakesignedList.setUniformItemSizes(False)

        self.nusLayout.addWidget(self.fakesigned, 0, 2, 1, 1)

        self.sysmenus = QGroupBox(self.gridLayoutWidget)
        self.sysmenus.setObjectName(u"sysmenus")
        sizePolicy1.setHeightForWidth(self.sysmenus.sizePolicy().hasHeightForWidth())
        self.sysmenus.setSizePolicy(sizePolicy1)
        self.sysmenus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sysmenuList = QListWidget(self.sysmenus)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        QListWidgetItem(self.sysmenuList)
        self.sysmenuList.setObjectName(u"sysmenuList")
        self.sysmenuList.setGeometry(QRect(0, 21, 263, 316))
        sizePolicy.setHeightForWidth(self.sysmenuList.sizePolicy().hasHeightForWidth())
        self.sysmenuList.setSizePolicy(sizePolicy)
        self.sysmenuList.setAlternatingRowColors(True)
        self.sysmenuList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.sysmenuList.setUniformItemSizes(False)

        self.nusLayout.addWidget(self.sysmenus, 0, 0, 1, 1)

        self.tabWidget.addTab(self.nus, "")
        self.wiiHax = QWidget()
        self.wiiHax.setObjectName(u"wiiHax")
        self.gridLayoutWidget_2 = QWidget(self.wiiHax)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 800, 681))
        self.wiiHaxLayout = QGridLayout(self.gridLayoutWidget_2)
        self.wiiHaxLayout.setObjectName(u"wiiHaxLayout")
        self.wiiHaxLayout.setContentsMargins(0, 0, 0, 0)
        self.wiiHomebrew = QGroupBox(self.gridLayoutWidget_2)
        self.wiiHomebrew.setObjectName(u"wiiHomebrew")
        sizePolicy1.setHeightForWidth(self.wiiHomebrew.sizePolicy().hasHeightForWidth())
        self.wiiHomebrew.setSizePolicy(sizePolicy1)
        self.wiiHomebrew.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wiiHomebrewList = QListView(self.wiiHomebrew)
        self.wiiHomebrewList.setObjectName(u"wiiHomebrewList")
        self.wiiHomebrewList.setGeometry(QRect(0, 21, 262, 316))
        sizePolicy.setHeightForWidth(self.wiiHomebrewList.sizePolicy().hasHeightForWidth())
        self.wiiHomebrewList.setSizePolicy(sizePolicy)
        self.wiiHomebrewList.setAlternatingRowColors(True)
        self.wiiHomebrewList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.wiiHomebrewList.setProperty(u"isWrapping", False)
        self.wiiHomebrewList.setUniformItemSizes(False)

        self.wiiHaxLayout.addWidget(self.wiiHomebrew, 0, 1, 1, 1)

        self.exploits = QGroupBox(self.gridLayoutWidget_2)
        self.exploits.setObjectName(u"exploits")
        sizePolicy1.setHeightForWidth(self.exploits.sizePolicy().hasHeightForWidth())
        self.exploits.setSizePolicy(sizePolicy1)
        self.exploits.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exploitList = QListView(self.exploits)
        self.exploitList.setObjectName(u"exploitList")
        self.exploitList.setGeometry(QRect(0, 21, 262, 316))
        sizePolicy.setHeightForWidth(self.exploitList.sizePolicy().hasHeightForWidth())
        self.exploitList.setSizePolicy(sizePolicy)
        self.exploitList.setAlternatingRowColors(True)
        self.exploitList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.exploitList.setUniformItemSizes(False)

        self.wiiHaxLayout.addWidget(self.exploits, 0, 0, 1, 1)

        self.vWiihomebrew = QGroupBox(self.gridLayoutWidget_2)
        self.vWiihomebrew.setObjectName(u"vWiihomebrew")
        sizePolicy1.setHeightForWidth(self.vWiihomebrew.sizePolicy().hasHeightForWidth())
        self.vWiihomebrew.setSizePolicy(sizePolicy1)
        self.vWiihomebrew.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vWiihomebrewList = QListView(self.vWiihomebrew)
        self.vWiihomebrewList.setObjectName(u"vWiihomebrewList")
        self.vWiihomebrewList.setGeometry(QRect(0, 21, 262, 315))
        sizePolicy.setHeightForWidth(self.vWiihomebrewList.sizePolicy().hasHeightForWidth())
        self.vWiihomebrewList.setSizePolicy(sizePolicy)
        self.vWiihomebrewList.setAlternatingRowColors(True)
        self.vWiihomebrewList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.vWiihomebrewList.setUniformItemSizes(False)

        self.wiiHaxLayout.addWidget(self.vWiihomebrew, 1, 1, 1, 1)

        self.hbc = QGroupBox(self.gridLayoutWidget_2)
        self.hbc.setObjectName(u"hbc")
        sizePolicy1.setHeightForWidth(self.hbc.sizePolicy().hasHeightForWidth())
        self.hbc.setSizePolicy(sizePolicy1)
        self.hbc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hbcList = QListView(self.hbc)
        self.hbcList.setObjectName(u"hbcList")
        self.hbcList.setGeometry(QRect(0, 21, 262, 315))
        sizePolicy.setHeightForWidth(self.hbcList.sizePolicy().hasHeightForWidth())
        self.hbcList.setSizePolicy(sizePolicy)
        self.hbcList.setAlternatingRowColors(True)
        self.hbcList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.hbcList.setProperty(u"isWrapping", False)
        self.hbcList.setUniformItemSizes(False)

        self.wiiHaxLayout.addWidget(self.hbc, 1, 0, 1, 1)

        self.bothHomebrew = QGroupBox(self.gridLayoutWidget_2)
        self.bothHomebrew.setObjectName(u"bothHomebrew")
        sizePolicy1.setHeightForWidth(self.bothHomebrew.sizePolicy().hasHeightForWidth())
        self.bothHomebrew.setSizePolicy(sizePolicy1)
        self.bothHomebrew.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bothHomebrewList = QListView(self.bothHomebrew)
        self.bothHomebrewList.setObjectName(u"bothHomebrewList")
        self.bothHomebrewList.setGeometry(QRect(0, 21, 262, 316))
        sizePolicy.setHeightForWidth(self.bothHomebrewList.sizePolicy().hasHeightForWidth())
        self.bothHomebrewList.setSizePolicy(sizePolicy)
        self.bothHomebrewList.setAlternatingRowColors(True)
        self.bothHomebrewList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.bothHomebrewList.setProperty(u"isWrapping", False)
        self.bothHomebrewList.setUniformItemSizes(False)

        self.wiiHaxLayout.addWidget(self.bothHomebrew, 0, 2, 1, 1)

        self.external = QGroupBox(self.gridLayoutWidget_2)
        self.external.setObjectName(u"external")
        self.external.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.externalText = QTextBrowser(self.external)
        self.externalText.setObjectName(u"externalText")
        self.externalText.setGeometry(QRect(0, 21, 262, 315))
        self.externalText.setOpenExternalLinks(True)
        self.externalText.setOpenLinks(False)

        self.wiiHaxLayout.addWidget(self.external, 1, 2, 1, 1)

        self.tabWidget.addTab(self.wiiHax, "")
        self.themes = QWidget()
        self.themes.setObjectName(u"themes")
        self.themeProtectWarning = QLabel(self.themes)
        self.themeProtectWarning.setObjectName(u"themeProtectWarning")
        self.themeProtectWarning.setGeometry(QRect(210, 630, 240, 60))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.themeProtectWarning.setFont(font)
        self.themeProtectWarning.setTextFormat(Qt.TextFormat.MarkdownText)
        self.themeProtectWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.themeProtectWarning.setWordWrap(True)
        self.themeProtectWarning.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.themeSysmenuWarning = QLabel(self.themes)
        self.themeSysmenuWarning.setObjectName(u"themeSysmenuWarning")
        self.themeSysmenuWarning.setGeometry(QRect(0, 630, 210, 60))
        self.themeSysmenuWarning.setFont(font)
        self.themeSysmenuWarning.setTextFormat(Qt.TextFormat.MarkdownText)
        self.themeSysmenuWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.themeSysmenuWarning.setWordWrap(True)
        self.themeSysmenuWarning.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.tabWidget.addTab(self.themes, "")
        self.cios = QWidget()
        self.cios.setObjectName(u"cios")
        self.gridLayoutWidget_3 = QWidget(self.cios)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 800, 634))
        self.ciosLayout = QGridLayout(self.gridLayoutWidget_3)
        self.ciosLayout.setObjectName(u"ciosLayout")
        self.ciosLayout.setContentsMargins(0, 0, 0, 0)
        self.wanin = waninCheckGrid(self.gridLayoutWidget_3)
        self.wanin.setObjectName(u"wanin")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.wanin.sizePolicy().hasHeightForWidth())
        self.wanin.setSizePolicy(sizePolicy2)
        self.wanin.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ciosLayout.addWidget(self.wanin, 0, 1, 2, 1)

        self.hermes = QGroupBox(self.gridLayoutWidget_3)
        self.hermes.setObjectName(u"hermes")
        self.hermes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hermesList = QListWidget(self.hermes)
        QListWidgetItem(self.hermesList)
        QListWidgetItem(self.hermesList)
        QListWidgetItem(self.hermesList)
        QListWidgetItem(self.hermesList)
        QListWidgetItem(self.hermesList)
        QListWidgetItem(self.hermesList)
        QListWidgetItem(self.hermesList)
        QListWidgetItem(self.hermesList)
        QListWidgetItem(self.hermesList)
        self.hermesList.setObjectName(u"hermesList")
        self.hermesList.setGeometry(QRect(0, 21, 262, 292))
        sizePolicy.setHeightForWidth(self.hermesList.sizePolicy().hasHeightForWidth())
        self.hermesList.setSizePolicy(sizePolicy)
        self.hermesList.setAlternatingRowColors(True)
        self.hermesList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.hermesList.setUniformItemSizes(False)

        self.ciosLayout.addWidget(self.hermes, 0, 2, 1, 1)

        self.d2x = d2xCheckGrid(self.gridLayoutWidget_3)
        self.d2x.setObjectName(u"d2x")
        self.d2x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ciosLayout.addWidget(self.d2x, 0, 0, 2, 1)

        self.cmios = QGroupBox(self.gridLayoutWidget_3)
        self.cmios.setObjectName(u"cmios")
        self.cmios.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cmiosList = QListWidget(self.cmios)
        QListWidgetItem(self.cmiosList)
        QListWidgetItem(self.cmiosList)
        QListWidgetItem(self.cmiosList)
        QListWidgetItem(self.cmiosList)
        QListWidgetItem(self.cmiosList)
        QListWidgetItem(self.cmiosList)
        self.cmiosList.setObjectName(u"cmiosList")
        self.cmiosList.setGeometry(QRect(0, 21, 262, 292))
        sizePolicy.setHeightForWidth(self.cmiosList.sizePolicy().hasHeightForWidth())
        self.cmiosList.setSizePolicy(sizePolicy)
        self.cmiosList.setAlternatingRowColors(True)
        self.cmiosList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.cmiosList.setUniformItemSizes(False)

        self.ciosLayout.addWidget(self.cmios, 1, 2, 1, 1)

        self.ciosWarning = QLabel(self.cios)
        self.ciosWarning.setObjectName(u"ciosWarning")
        self.ciosWarning.setGeometry(QRect(0, 630, 210, 60))
        font1 = QFont()
        font1.setBold(True)
        self.ciosWarning.setFont(font1)
        self.ciosWarning.setTextFormat(Qt.TextFormat.PlainText)
        self.ciosWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ciosWarning.setWordWrap(True)
        self.ciosWarning.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.ciosNote = QLabel(self.cios)
        self.ciosNote.setObjectName(u"ciosNote")
        self.ciosNote.setGeometry(QRect(210, 630, 220, 60))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(True)
        self.ciosNote.setFont(font2)
        self.ciosNote.setTextFormat(Qt.TextFormat.MarkdownText)
        self.ciosNote.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ciosNote.setWordWrap(True)
        self.ciosNote.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.d2xSettings = QPushButton(self.cios)
        self.d2xSettings.setObjectName(u"d2xSettings")
        self.d2xSettings.setGeometry(QRect(710, 635, 91, 50))
        self.wiiRecommended = QPushButton(self.cios)
        self.wiiRecommended.setObjectName(u"wiiRecommended")
        self.wiiRecommended.setGeometry(QRect(430, 635, 140, 50))
        self.vwiiRecommended = QPushButton(self.cios)
        self.vwiiRecommended.setObjectName(u"vwiiRecommended")
        self.vwiiRecommended.setGeometry(QRect(570, 635, 140, 50))
        self.tabWidget.addTab(self.cios, "")
        self.misc = QWidget()
        self.misc.setObjectName(u"misc")
        self.gridLayoutWidget_4 = QWidget(self.misc)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 0, 800, 681))
        self.miscLayout = QGridLayout(self.gridLayoutWidget_4)
        self.miscLayout.setObjectName(u"miscLayout")
        self.miscLayout.setContentsMargins(0, 0, 0, 0)
        self.pc = QGroupBox(self.gridLayoutWidget_4)
        self.pc.setObjectName(u"pc")
        sizePolicy1.setHeightForWidth(self.pc.sizePolicy().hasHeightForWidth())
        self.pc.setSizePolicy(sizePolicy1)
        self.pc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pcList = QListView(self.pc)
        self.pcList.setObjectName(u"pcList")
        self.pcList.setGeometry(QRect(0, 21, 396, 658))
        sizePolicy.setHeightForWidth(self.pcList.sizePolicy().hasHeightForWidth())
        self.pcList.setSizePolicy(sizePolicy)
        self.pcList.setAlternatingRowColors(True)
        self.pcList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.pcList.setUniformItemSizes(False)

        self.miscLayout.addWidget(self.pc, 0, 1, 1, 1)

        self.wiiu = QGroupBox(self.gridLayoutWidget_4)
        self.wiiu.setObjectName(u"wiiu")
        sizePolicy1.setHeightForWidth(self.wiiu.sizePolicy().hasHeightForWidth())
        self.wiiu.setSizePolicy(sizePolicy1)
        self.wiiu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wiiuList = QListView(self.wiiu)
        self.wiiuList.setObjectName(u"wiiuList")
        self.wiiuList.setGeometry(QRect(0, 21, 396, 658))
        sizePolicy.setHeightForWidth(self.wiiuList.sizePolicy().hasHeightForWidth())
        self.wiiuList.setSizePolicy(sizePolicy)
        self.wiiuList.setAlternatingRowColors(True)
        self.wiiuList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.wiiuList.setUniformItemSizes(False)

        self.miscLayout.addWidget(self.wiiu, 0, 0, 1, 1)

        self.tabWidget.addTab(self.misc, "")
        self.warning = QLabel(self.centralwidget)
        self.warning.setObjectName(u"warning")
        self.warning.setGeometry(QRect(0, 720, 290, 50))
        self.warning.setFont(font1)
        self.warning.setTextFormat(Qt.TextFormat.MarkdownText)
        self.warning.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.warning.setWordWrap(True)
        self.warning.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.download = QPushButton(self.centralwidget)
        self.download.setObjectName(u"download")
        self.download.setGeometry(QRect(690, 720, 110, 50))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.download.setIcon(icon1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tabWidget, self.sysmenuList)
        QWidget.setTabOrder(self.sysmenuList, self.realsignedList)
        QWidget.setTabOrder(self.realsignedList, self.fakesignedList)
        QWidget.setTabOrder(self.fakesignedList, self.contentList)
        QWidget.setTabOrder(self.contentList, self.channelList)
        QWidget.setTabOrder(self.channelList, self.otherList)
        QWidget.setTabOrder(self.otherList, self.exploitList)
        QWidget.setTabOrder(self.exploitList, self.wiiHomebrewList)
        QWidget.setTabOrder(self.wiiHomebrewList, self.bothHomebrewList)
        QWidget.setTabOrder(self.bothHomebrewList, self.hbcList)
        QWidget.setTabOrder(self.hbcList, self.vWiihomebrewList)
        QWidget.setTabOrder(self.vWiihomebrewList, self.externalText)
        QWidget.setTabOrder(self.externalText, self.hermesList)
        QWidget.setTabOrder(self.hermesList, self.cmiosList)
        QWidget.setTabOrder(self.cmiosList, self.wiiRecommended)
        QWidget.setTabOrder(self.wiiRecommended, self.vwiiRecommended)
        QWidget.setTabOrder(self.vwiiRecommended, self.d2xSettings)
        QWidget.setTabOrder(self.d2xSettings, self.wiiuList)
        QWidget.setTabOrder(self.wiiuList, self.pcList)
        QWidget.setTabOrder(self.pcList, self.download)

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"ModMii", None))
        self.channels.setTitle(QCoreApplication.translate("mainWindow", u"Channels", None))

        __sortingEnabled = self.channelList.isSortingEnabled()
        self.channelList.setSortingEnabled(False)
        ___qlistwidgetitem = self.channelList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("mainWindow", u"4.1U", None));
        ___qlistwidgetitem1 = self.channelList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("mainWindow", u"New Item", None));
        ___qlistwidgetitem2 = self.channelList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("mainWindow", u"New Item", None));
        ___qlistwidgetitem3 = self.channelList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("mainWindow", u"New Item", None));
        ___qlistwidgetitem4 = self.channelList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("mainWindow", u"4.2U", None));
        ___qlistwidgetitem5 = self.channelList.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("mainWindow", u"4.3U", None));
        ___qlistwidgetitem6 = self.channelList.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("mainWindow", u"4.1E", None));
        ___qlistwidgetitem7 = self.channelList.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("mainWindow", u"4.2E", None));
        ___qlistwidgetitem8 = self.channelList.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("mainWindow", u"4.3E", None));
        ___qlistwidgetitem9 = self.channelList.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("mainWindow", u"4.1J", None));
        ___qlistwidgetitem10 = self.channelList.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("mainWindow", u"4.2J", None));
        ___qlistwidgetitem11 = self.channelList.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("mainWindow", u"4.3J", None));
        ___qlistwidgetitem12 = self.channelList.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("mainWindow", u"4.1K", None));
        ___qlistwidgetitem13 = self.channelList.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("mainWindow", u"4.2K", None));
        ___qlistwidgetitem14 = self.channelList.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("mainWindow", u"4.3K", None));
        ___qlistwidgetitem15 = self.channelList.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("mainWindow", u"vWii 4.3U (5.2.0)", None));
        ___qlistwidgetitem16 = self.channelList.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("mainWindow", u"vWii 4.3E (5.2.0)", None));
        ___qlistwidgetitem17 = self.channelList.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("mainWindow", u"vWii 4.3J (5.2.0)", None));
        ___qlistwidgetitem18 = self.channelList.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("mainWindow", u"New Item", None));
        self.channelList.setSortingEnabled(__sortingEnabled)

        self.contents.setTitle(QCoreApplication.translate("mainWindow", u"Content Files", None))

        __sortingEnabled1 = self.contentList.isSortingEnabled()
        self.contentList.setSortingEnabled(False)
        ___qlistwidgetitem19 = self.contentList.item(0)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("mainWindow", u"0e.app [IOS80 v6943]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem19.setToolTip(QCoreApplication.translate("mainWindow", u"Used to construct NEEK for Wii.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem20 = self.contentList.item(1)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("mainWindow", u"01.app [IOS60 v6174]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem20.setToolTip(QCoreApplication.translate("mainWindow", u"Used to construct older versions of NEEK+DI (before v186) and NEEK2O+DI (before v70) for Wii.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem21 = self.contentList.item(2)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("mainWindow", u"0d.app [vIOS80 v7200]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem21.setToolTip(QCoreApplication.translate("mainWindow", u"Used to construct NEEK for vWii.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem22 = self.contentList.item(3)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("mainWindow", u"0c.app [MIOS v10]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem22.setToolTip(QCoreApplication.translate("mainWindow", u"Used to construct DIOS MIOS for Wii.", None));
#endif // QT_CONFIG(tooltip)
        self.contentList.setSortingEnabled(__sortingEnabled1)

        self.realsigned.setTitle(QCoreApplication.translate("mainWindow", u"Non-Fakesigned IOSs\\MIOS", None))

        __sortingEnabled2 = self.realsignedList.isSortingEnabled()
        self.realsignedList.setSortingEnabled(False)
        ___qlistwidgetitem23 = self.realsignedList.item(0)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("mainWindow", u"IOS9 v1034", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem23.setToolTip(QCoreApplication.translate("mainWindow", u"IOS9 is used by System Menu 1.0 and early games like Zelda: Twilight Princess, Wii Sports, Wii Play, WarioWare: Smooth Moves.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem24 = self.realsignedList.item(1)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("mainWindow", u"IOS12 v526", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem24.setToolTip(QCoreApplication.translate("mainWindow", u"IOS12 is an IOS that was previously thought to be the oldest, used by titles such as Elebits.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem25 = self.realsignedList.item(2)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("mainWindow", u"IOS13 v1032", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem25.setToolTip(QCoreApplication.translate("mainWindow", u"IOS13 is used by Photo Channel 1.0.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem26 = self.realsignedList.item(3)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("mainWindow", u"IOS14 v1032", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem26.setToolTip(QCoreApplication.translate("mainWindow", u"IOS14 is used by Pok\u00e9mon Battle Revolution (Japanese version only).", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem27 = self.realsignedList.item(4)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("mainWindow", u"IOS15 v1032", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem27.setToolTip(QCoreApplication.translate("mainWindow", u"IOS15 was previously used by some official channels; it has not been stubbed because the Internet Channel, which could not be updated through standard updates, previously used it.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem28 = self.realsignedList.item(5)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("mainWindow", u"IOS17 v1032", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem28.setToolTip(QCoreApplication.translate("mainWindow", u"IOS17 is used by early titles such as Bust-A-Move Bash and Super Paper Mario.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem29 = self.realsignedList.item(6)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("mainWindow", u"IOS21 v1039", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem29.setToolTip(QCoreApplication.translate("mainWindow", u"IOS21 is used by third party games (No More Heroes). many other games such as Wii Sports were also re-released under this IOS.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem30 = self.realsignedList.item(7)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("mainWindow", u"IOS22 v1294", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem30.setToolTip(QCoreApplication.translate("mainWindow", u"IOS22 is used by a few games like High School Musical: Sing It! and Boogie.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem31 = self.realsignedList.item(8)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("mainWindow", u"IOS28 v1807", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem31.setToolTip(QCoreApplication.translate("mainWindow", u"IOS28 is only used by Metroid Prime 3: Corruption. The first IOS released in modular parts.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem32 = self.realsignedList.item(9)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("mainWindow", u"IOS30 v2576", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem32.setToolTip(QCoreApplication.translate("mainWindow", u"IOS30 is used by System Menu 3.0-3.3. Officially this IOS is stubbed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem33 = self.realsignedList.item(10)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("mainWindow", u"IOS31 v3608", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem33.setToolTip(QCoreApplication.translate("mainWindow", u"IOS31 is used by News & Weather channels. RC24 (WiiLink predecessor) used to require a patched version of IOS31 so it could download custom News & Weather data.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem34 = self.realsignedList.item(11)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("mainWindow", u"IOS33 v3608", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem34.setToolTip(QCoreApplication.translate("mainWindow", u"IOS33 is an IOS version based on IOS31 and used in games like Super Mario Galaxy.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem35 = self.realsignedList.item(12)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("mainWindow", u"IOS34 v3608", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem35.setToolTip(QCoreApplication.translate("mainWindow", u"IOS34 is used by Internet Channel v257.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem36 = self.realsignedList.item(13)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("mainWindow", u"IOS35 v3608", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem36.setToolTip(QCoreApplication.translate("mainWindow", u"IOS35 is a copy of IOS31 used by games like Call of Duty, Wii Music, etc.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem37 = self.realsignedList.item(14)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("mainWindow", u"IOS36 v3351", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem37.setToolTip(QCoreApplication.translate("mainWindow", u"IOS36 v3351 was the first IOS patched to restore the trucha bug, enabling custom IOS installation. Today it is recommended not to patch IOS36.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem38 = self.realsignedList.item(15)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("mainWindow", u"IOS36 v3608", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem38.setToolTip(QCoreApplication.translate("mainWindow", u"IOS36 v3608 is used by titles such as Super Smash Bros. Brawl and Mario Kart Wii", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem39 = self.realsignedList.item(16)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("mainWindow", u"IOS37 v5663", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem39.setToolTip(QCoreApplication.translate("mainWindow", u"IOS37 is used by several WiiWare games and older Guitar Hero/Rock Band games.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem40 = self.realsignedList.item(17)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("mainWindow", u"IOS38 v4124", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem40.setToolTip(QCoreApplication.translate("mainWindow", u"IOS38 is used by Animal Crossing: City Folk and the Nintendo Wii Speak Channel.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem41 = self.realsignedList.item(18)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("mainWindow", u"IOS41 v3607", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem41.setToolTip(QCoreApplication.translate("mainWindow", u"IOS41 is a Korea-specific IOS used by preinstalled channels. It is identical to IOS45.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem42 = self.realsignedList.item(19)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("mainWindow", u"IOS43 v3607", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem42.setToolTip(QCoreApplication.translate("mainWindow", u"IOS43 is only used by some Korean games.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem43 = self.realsignedList.item(20)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("mainWindow", u"IOS45 v3607", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem43.setToolTip(QCoreApplication.translate("mainWindow", u"IOS45 is only used by some Korean games. It is identical to IOS41.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem44 = self.realsignedList.item(21)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("mainWindow", u"IOS46 v3607", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem44.setToolTip(QCoreApplication.translate("mainWindow", u"IOS46 is an IOS used by some Korean games like Mario Kart Wii and Need for Speed Undercover.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem45 = self.realsignedList.item(22)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("mainWindow", u"IOS48 v4124", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem45.setToolTip(QCoreApplication.translate("mainWindow", u"IOS48 is used by Animal Crossing: City Folk (Korean version only).", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem46 = self.realsignedList.item(23)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("mainWindow", u"IOS53 v5663", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem46.setToolTip(QCoreApplication.translate("mainWindow", u"IOS53 is used by titles such as New Super Mario Bros. Wii and Wii Fit Plus.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem47 = self.realsignedList.item(24)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("mainWindow", u"IOS55 v5663", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem47.setToolTip(QCoreApplication.translate("mainWindow", u"IOS55 is used by titles such as Wii Sports Resort and The Conduit.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem48 = self.realsignedList.item(25)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("mainWindow", u"IOS56 v5662", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem48.setToolTip(QCoreApplication.translate("mainWindow", u"IOS56 added SDHC support and is identical to IOS61. Used by Wii Speak 2.0 and the latest Shopping Channel.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem49 = self.realsignedList.item(26)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("mainWindow", u"IOS57 v5919", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem49.setToolTip(QCoreApplication.translate("mainWindow", u"IOS57 is used by many of the newer games released near the end of the production of Wii discs in 2020, although it was originally released in 2009.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem50 = self.realsignedList.item(27)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("mainWindow", u"IOS58 v6176", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem50.setToolTip(QCoreApplication.translate("mainWindow", u"IOS58 offers improved USB2 speeds and is preferred by many apps including the Homebrew Channel.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem51 = self.realsignedList.item(28)
        ___qlistwidgetitem51.setText(QCoreApplication.translate("mainWindow", u"IOS59 v9249", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem51.setToolTip(QCoreApplication.translate("mainWindow", u"IOS59 is a Japan exclusive IOS. ModMii Wizards will only direct Japanese consoles to install it.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem52 = self.realsignedList.item(29)
        ___qlistwidgetitem52.setText(QCoreApplication.translate("mainWindow", u"IOS60 v6174", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem52.setToolTip(QCoreApplication.translate("mainWindow", u"IOS60 is used by System Menu 4.0 & 4.1. First to support SDHC. Officially this IOS is stubbed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem53 = self.realsignedList.item(30)
        ___qlistwidgetitem53.setText(QCoreApplication.translate("mainWindow", u"IOS61 v5662", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem53.setToolTip(QCoreApplication.translate("mainWindow", u"IOS61 was used by the Wii Shop Channel from the System Menu 4.0-4.2 updates. Also used by Photo Channel 1.1b. It is identical to IOS56.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem54 = self.realsignedList.item(31)
        ___qlistwidgetitem54.setText(QCoreApplication.translate("mainWindow", u"IOS62 v6430", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem54.setToolTip(QCoreApplication.translate("mainWindow", u"IOS62 is used by the Wii U Transfer Tool.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem55 = self.realsignedList.item(32)
        ___qlistwidgetitem55.setText(QCoreApplication.translate("mainWindow", u"IOS70 v6687", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem55.setToolTip(QCoreApplication.translate("mainWindow", u"IOS70 is used by System Menu 4.2. Officially this IOS is stubbed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem56 = self.realsignedList.item(33)
        ___qlistwidgetitem56.setText(QCoreApplication.translate("mainWindow", u"IOS80 v6944", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem56.setToolTip(QCoreApplication.translate("mainWindow", u"IOS80 is used by System Menu 4.3.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem57 = self.realsignedList.item(34)
        ___qlistwidgetitem57.setText(QCoreApplication.translate("mainWindow", u"MIOS v10", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem57.setToolTip(QCoreApplication.translate("mainWindow", u"MIOS is a special version of IOS that runs when the Wii enters GameCube mode", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem58 = self.realsignedList.item(35)
        ___qlistwidgetitem58.setText(QCoreApplication.translate("mainWindow", u"vWii IOSs [x29]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem58.setToolTip(QCoreApplication.translate("mainWindow", u"Download 29 IOSs for vWii:\n"
"                                                                              vIOS9, 12, 13, 14, 15, 17, 21, 22, 28, 31, 33, 34, 35, 36, 37, 38, 41, 43, 45, 46, 48, 53, 55, 56, 57, 58, 59, 62 & 80.\n"
"\n"
"                                                                              While effectively these IOSs are not patched, technically they are fakesigned and re-encrypted to use the Wii retail common key so that they can be installed using WAD Managers available today.\n"
"\n"
"                                                                              ...I know what you're thinking and the answer is yes, shortcuts were taken.", None));
#endif // QT_CONFIG(tooltip)
        self.realsignedList.setSortingEnabled(__sortingEnabled2)

        self.other.setTitle(QCoreApplication.translate("mainWindow", u"Other WADs", None))

        __sortingEnabled3 = self.otherList.isSortingEnabled()
        self.otherList.setSortingEnabled(False)
        ___qlistwidgetitem59 = self.otherList.item(0)
        ___qlistwidgetitem59.setText(QCoreApplication.translate("mainWindow", u"4.1E", None));
        ___qlistwidgetitem60 = self.otherList.item(1)
        ___qlistwidgetitem60.setText(QCoreApplication.translate("mainWindow", u"4.2E", None));
        ___qlistwidgetitem61 = self.otherList.item(2)
        ___qlistwidgetitem61.setText(QCoreApplication.translate("mainWindow", u"4.3E", None));
        ___qlistwidgetitem62 = self.otherList.item(3)
        ___qlistwidgetitem62.setText(QCoreApplication.translate("mainWindow", u"4.1J", None));
        ___qlistwidgetitem63 = self.otherList.item(4)
        ___qlistwidgetitem63.setText(QCoreApplication.translate("mainWindow", u"4.2J", None));
        ___qlistwidgetitem64 = self.otherList.item(5)
        ___qlistwidgetitem64.setText(QCoreApplication.translate("mainWindow", u"4.3J", None));
        ___qlistwidgetitem65 = self.otherList.item(6)
        ___qlistwidgetitem65.setText(QCoreApplication.translate("mainWindow", u"4.1K", None));
        ___qlistwidgetitem66 = self.otherList.item(7)
        ___qlistwidgetitem66.setText(QCoreApplication.translate("mainWindow", u"4.2K", None));
        ___qlistwidgetitem67 = self.otherList.item(8)
        ___qlistwidgetitem67.setText(QCoreApplication.translate("mainWindow", u"4.3K", None));
        ___qlistwidgetitem68 = self.otherList.item(9)
        ___qlistwidgetitem68.setText(QCoreApplication.translate("mainWindow", u"vWii 4.3U (5.2.0)", None));
        ___qlistwidgetitem69 = self.otherList.item(10)
        ___qlistwidgetitem69.setText(QCoreApplication.translate("mainWindow", u"vWii 4.3E (5.2.0)", None));
        ___qlistwidgetitem70 = self.otherList.item(11)
        ___qlistwidgetitem70.setText(QCoreApplication.translate("mainWindow", u"vWii 4.3J (5.2.0)", None));
        self.otherList.setSortingEnabled(__sortingEnabled3)

        self.fakesigned.setTitle(QCoreApplication.translate("mainWindow", u"Fakesigned IOSs", None))

        __sortingEnabled4 = self.fakesignedList.isSortingEnabled()
        self.fakesignedList.setSortingEnabled(False)
        ___qlistwidgetitem71 = self.fakesignedList.item(0)
        ___qlistwidgetitem71.setText(QCoreApplication.translate("mainWindow", u"IOS11[60]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem71.setToolTip(QCoreApplication.translate("mainWindow", u"IOS11 is used by System Menu 2.0 & 2.1; this IOS is based on IOS60 to maximize compatibility and protection. Officially this IOS is stubbed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem72 = self.fakesignedList.item(1)
        ___qlistwidgetitem72.setText(QCoreApplication.translate("mainWindow", u"IOS20[60]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem72.setToolTip(QCoreApplication.translate("mainWindow", u"IOS20 is used by System Menu 2.2; this IOS is based on IOS60 to maximize compatibility and protection. Officially this IOS is stubbed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem73 = self.fakesignedList.item(2)
        ___qlistwidgetitem73.setText(QCoreApplication.translate("mainWindow", u"IOS30[60]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem73.setToolTip(QCoreApplication.translate("mainWindow", u"IOS30 is used by System Menu 3.0-3.3; this IOS is based on IOS60 to maximize compatibility and protection. Officially this IOS is stubbed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem74 = self.fakesignedList.item(3)
        ___qlistwidgetitem74.setText(QCoreApplication.translate("mainWindow", u"IOS40[60]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem74.setToolTip(QCoreApplication.translate("mainWindow", u"IOS40 is used by System Menu 3.3 for all Korean consoles; this IOS is based on IOS60 to maximize compatibility and protection. Officially this IOS is stubbed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem75 = self.fakesignedList.item(4)
        ___qlistwidgetitem75.setText(QCoreApplication.translate("mainWindow", u"IOS50[60]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem75.setToolTip(QCoreApplication.translate("mainWindow", u"IOS50 is used by System Menu 3.4; this IOS is based on IOS60 to maximize compatibility and protection. Officially this IOS is stubbed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem76 = self.fakesignedList.item(5)
        ___qlistwidgetitem76.setText(QCoreApplication.translate("mainWindow", u"IOS52[60]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem76.setToolTip(QCoreApplication.translate("mainWindow", u"IOS52 is used by System Menu 3.5 and exclusive to Korea; this IOS is based on IOS60 to maximize compatibility and protection. Officially this IOS is stubbed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem77 = self.fakesignedList.item(6)
        ___qlistwidgetitem77.setText(QCoreApplication.translate("mainWindow", u"IOS60[60]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem77.setToolTip(QCoreApplication.translate("mainWindow", u"IOS60 is used by System Menu 4.0 & 4.1. Officially this IOS is stubbed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem78 = self.fakesignedList.item(7)
        ___qlistwidgetitem78.setText(QCoreApplication.translate("mainWindow", u"IOS70[60]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem78.setToolTip(QCoreApplication.translate("mainWindow", u"IOS70 is used by System Menu 4.2; this IOS is based on IOS60 to maximize compatibility and protection. Officially this IOS is stubbed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem79 = self.fakesignedList.item(8)
        ___qlistwidgetitem79.setText(QCoreApplication.translate("mainWindow", u"IOS80[60]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem79.setToolTip(QCoreApplication.translate("mainWindow", u"IOS80 is used by System Menu 4.3; this IOS is based on IOS60 to maximize compatibility and protection.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem80 = self.fakesignedList.item(9)
        ___qlistwidgetitem80.setText(QCoreApplication.translate("mainWindow", u"IOS236[36]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem80.setToolTip(QCoreApplication.translate("mainWindow", u"IOS236 is a patched version of IOS36. It is no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem81 = self.fakesignedList.item(10)
        ___qlistwidgetitem81.setText(QCoreApplication.translate("mainWindow", u"vIOS61[56]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem81.setToolTip(QCoreApplication.translate("mainWindow", u"vIOS61 (aka cIOS61[56]-v5918-vWii) is a not normally found on vWii. It is a custom copy of vIOS56 with only it's slot changed to 61 to support Photo Channel 1.1.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem82 = self.fakesignedList.item(11)
        ___qlistwidgetitem82.setText(QCoreApplication.translate("mainWindow", u"vIOS80[80]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem82.setToolTip(QCoreApplication.translate("mainWindow", u"vIOS80 is used by vWii System Menu 4.3.", None));
#endif // QT_CONFIG(tooltip)
        self.fakesignedList.setSortingEnabled(__sortingEnabled4)

        self.sysmenus.setTitle(QCoreApplication.translate("mainWindow", u"System Menus", None))

        __sortingEnabled5 = self.sysmenuList.isSortingEnabled()
        self.sysmenuList.setSortingEnabled(False)
        ___qlistwidgetitem83 = self.sysmenuList.item(0)
        ___qlistwidgetitem83.setText(QCoreApplication.translate("mainWindow", u"4.1U", None));
        ___qlistwidgetitem84 = self.sysmenuList.item(1)
        ___qlistwidgetitem84.setText(QCoreApplication.translate("mainWindow", u"4.2U", None));
        ___qlistwidgetitem85 = self.sysmenuList.item(2)
        ___qlistwidgetitem85.setText(QCoreApplication.translate("mainWindow", u"4.3U", None));
        ___qlistwidgetitem86 = self.sysmenuList.item(3)
        ___qlistwidgetitem86.setText(QCoreApplication.translate("mainWindow", u"4.1E", None));
        ___qlistwidgetitem87 = self.sysmenuList.item(4)
        ___qlistwidgetitem87.setText(QCoreApplication.translate("mainWindow", u"4.2E", None));
        ___qlistwidgetitem88 = self.sysmenuList.item(5)
        ___qlistwidgetitem88.setText(QCoreApplication.translate("mainWindow", u"4.3E", None));
        ___qlistwidgetitem89 = self.sysmenuList.item(6)
        ___qlistwidgetitem89.setText(QCoreApplication.translate("mainWindow", u"4.1J", None));
        ___qlistwidgetitem90 = self.sysmenuList.item(7)
        ___qlistwidgetitem90.setText(QCoreApplication.translate("mainWindow", u"4.2J", None));
        ___qlistwidgetitem91 = self.sysmenuList.item(8)
        ___qlistwidgetitem91.setText(QCoreApplication.translate("mainWindow", u"4.3J", None));
        ___qlistwidgetitem92 = self.sysmenuList.item(9)
        ___qlistwidgetitem92.setText(QCoreApplication.translate("mainWindow", u"4.1K", None));
        ___qlistwidgetitem93 = self.sysmenuList.item(10)
        ___qlistwidgetitem93.setText(QCoreApplication.translate("mainWindow", u"4.2K", None));
        ___qlistwidgetitem94 = self.sysmenuList.item(11)
        ___qlistwidgetitem94.setText(QCoreApplication.translate("mainWindow", u"4.3K", None));
        ___qlistwidgetitem95 = self.sysmenuList.item(12)
        ___qlistwidgetitem95.setText(QCoreApplication.translate("mainWindow", u"vWii 4.3U (5.2.0)", None));
        ___qlistwidgetitem96 = self.sysmenuList.item(13)
        ___qlistwidgetitem96.setText(QCoreApplication.translate("mainWindow", u"vWii 4.3E (5.2.0)", None));
        ___qlistwidgetitem97 = self.sysmenuList.item(14)
        ___qlistwidgetitem97.setText(QCoreApplication.translate("mainWindow", u"vWii 4.3J (5.2.0)", None));
        self.sysmenuList.setSortingEnabled(__sortingEnabled5)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.nus), QCoreApplication.translate("mainWindow", u"NUS Files", None))
        self.wiiHomebrew.setTitle(QCoreApplication.translate("mainWindow", u"Wii-Only Homebrew", None))
        self.exploits.setTitle(QCoreApplication.translate("mainWindow", u"Exploits", None))
        self.vWiihomebrew.setTitle(QCoreApplication.translate("mainWindow", u"vWii-Only Homebrew", None))
        self.hbc.setTitle(QCoreApplication.translate("mainWindow", u"Homebrew Channels", None))
        self.bothHomebrew.setTitle(QCoreApplication.translate("mainWindow", u"Wii && vWii Homebrew", None))
        self.external.setTitle(QCoreApplication.translate("mainWindow", u"Externally linked", None))
        self.externalText.setMarkdown(QCoreApplication.translate("mainWindow", u"[BlueBomb \\[U\\\\E\\\\J\\\\K]](https://wii.hacks.guide/bluebomb.html)                \n"
"                                                       \n"
"\n"
"[szsHaxx \\[U\\\\E\\\\J\\\\K]](https://github.com/MikeIsAStar/szsHaxx)\n"
"\n"
"", None))
        self.externalText.setHtml(QCoreApplication.translate("mainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://wii.hacks.guide/bluebomb.html\"><span style=\" text-decoration: underline; color:#1d99f3;\">BlueBomb [U\\E\\J\\K]</span></a>                                                                        </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/MikeIsAStar/szsHaxx\"><sp"
                        "an style=\" text-decoration: underline; color:#1d99f3;\">szsHaxx [U\\E\\J\\K]</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wiiHax), QCoreApplication.translate("mainWindow", u"Wii && vWii Homebrew && Exploits", None))
        self.themeProtectWarning.setText(QCoreApplication.translate("mainWindow", u" DON'T INSTALL THEMES WITHOUT PROTECTION: _BOOTMII, PRIILOADER AND NAND BACKUP_", None))
        self.themeSysmenuWarning.setText(QCoreApplication.translate("mainWindow", u"ONLY INSTALL THEMES FOR _YOUR SPECIFIC SYSTEM MENU VERSION AND REGION!_", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.themes), QCoreApplication.translate("mainWindow", u"System Menu Themes", None))
        self.wanin.setTitle(QCoreApplication.translate("mainWindow", u"Waninkoko cIOSs", None))
        self.hermes.setTitle(QCoreApplication.translate("mainWindow", u"Hermes cIOSs", None))

        __sortingEnabled6 = self.hermesList.isSortingEnabled()
        self.hermesList.setSortingEnabled(False)
        ___qlistwidgetitem98 = self.hermesList.item(0)
        ___qlistwidgetitem98.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5.1 cIOS202 [60]\u2661", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem98.setToolTip(QCoreApplication.translate("mainWindow", u"\u2661Semi-Recommended cIOS. It is the ideal cIOS for slot 202 however it is outdated: cIOS202 was used for older versions of some popular emulators.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem99 = self.hermesList.item(1)
        ___qlistwidgetitem99.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5.1 cIOS222 [38]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem99.setToolTip(QCoreApplication.translate("mainWindow", u"Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem100 = self.hermesList.item(2)
        ___qlistwidgetitem100.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5.1 cIOS223 [37]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem100.setToolTip(QCoreApplication.translate("mainWindow", u"Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem101 = self.hermesList.item(3)
        ___qlistwidgetitem101.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5.1 cIOS224 [57]\u2661", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem101.setToolTip(QCoreApplication.translate("mainWindow", u"\u2661Semi-Recommended cIOS. It is the ideal cIOS for slot 224 however it is outdated. Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem102 = self.hermesList.item(4)
        ___qlistwidgetitem102.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5 cIOS222 [38]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem102.setToolTip(QCoreApplication.translate("mainWindow", u"Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem103 = self.hermesList.item(5)
        ___qlistwidgetitem103.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5 cIOS223 [37]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem103.setToolTip(QCoreApplication.translate("mainWindow", u"Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem104 = self.hermesList.item(6)
        ___qlistwidgetitem104.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5 cIOS224 [57]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem104.setToolTip(QCoreApplication.translate("mainWindow", u"Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem105 = self.hermesList.item(7)
        ___qlistwidgetitem105.setText(QCoreApplication.translate("mainWindow", u"Hermes-v4 cIOS222 [38]\u2661", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem105.setToolTip(QCoreApplication.translate("mainWindow", u"\u2661Semi-Recommended cIOS. It is the ideal cIOS for slot 222 however it is outdated. Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem106 = self.hermesList.item(8)
        ___qlistwidgetitem106.setText(QCoreApplication.translate("mainWindow", u"Hermes-v4 cIOS223 [37+38]\u2661", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem106.setToolTip(QCoreApplication.translate("mainWindow", u"\u2661Semi-Recommended cIOS. It is the ideal cIOS for slot 223 and was widely used for compatibility with guitar-hero games however it is outdated. Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        self.hermesList.setSortingEnabled(__sortingEnabled6)

        self.d2x.setTitle(QCoreApplication.translate("mainWindow", u"d2x-d2xversion cIOSs", None))
        self.cmios.setTitle(QCoreApplication.translate("mainWindow", u"cMIOSs", None))

        __sortingEnabled7 = self.cmiosList.isSortingEnabled()
        self.cmiosList.setSortingEnabled(False)
        ___qlistwidgetitem107 = self.cmiosList.item(0)
        ___qlistwidgetitem107.setText(QCoreApplication.translate("mainWindow", u"Swiss cMIOS r1788 [10]\u2661", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem107.setToolTip(QCoreApplication.translate("mainWindow", u"Semi-Recommended cMIOS. A cMIOS with Swiss r1788 built-in. Hold Y during any GameCube mode load to start the built-in Swiss.  If Y is not held, then it should behave identically to WiiGator\\WiiPower's cMIOS and official MIOS. While this is the ideal cMIOS, because of Nintendont, cMIOSs are generally not needed, unless loading backup Gamecube discs on older compatible Wiis.\n"
"\n"
"                                                                              Based on MIOSv10.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem108 = self.cmiosList.item(1)
        ___qlistwidgetitem108.setText(QCoreApplication.translate("mainWindow", u"WiiGator\\Power cMIOS-v0.2 [10]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem108.setToolTip(QCoreApplication.translate("mainWindow", u"Since Nintendont, cMIOSs are generally not needed, unless loading backup Gamecube discs on older compatible Wiis.\n"
"\n"
"                                                                              Based on MIOSv10.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem109 = self.cmiosList.item(2)
        ___qlistwidgetitem109.setText(QCoreApplication.translate("mainWindow", u"WiiGator cMIOS-v0.2 [4]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem109.setToolTip(QCoreApplication.translate("mainWindow", u"Since Nintendont, cMIOSs are generally not needed, unless loading backup Gamecube discs on older compatible Wiis.\n"
"\n"
"                                                                              Based on MIOSv4.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem110 = self.cmiosList.item(3)
        ___qlistwidgetitem110.setText(QCoreApplication.translate("mainWindow", u"Waninkoko cMIOS-rev5 [4]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem110.setToolTip(QCoreApplication.translate("mainWindow", u"Since Nintendont, cMIOSs are generally not needed, unless loading backup Gamecube discs on older compatible Wiis.\n"
"\n"
"                                                                              Based on MIOSv4.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem111 = self.cmiosList.item(4)
        ___qlistwidgetitem111.setText(QCoreApplication.translate("mainWindow", u"DIOS MIOS Lite (DML) v2.11", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem111.setToolTip(QCoreApplication.translate("mainWindow", u"Since Nintendont, DML is generally not used anymore.\n"
"\n"
"                                                                              DML (Dios Mios Lite) is a tool which allows you to run Gamecube games from an SD Card.\n"
"\n"
"                                                                              Note: for DML to work with SNEEK+DI the WAD must be installed to real NAND and accessed via an emulated NAND.\n"
"\n"
"                                                                              Games must be in discex format, use discex or ModMii's Game Bulk Extractor.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem112 = self.cmiosList.item(5)
        ___qlistwidgetitem112.setText(QCoreApplication.translate("mainWindow", u"DIOS MIOS v2.11", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem112.setToolTip(QCoreApplication.translate("mainWindow", u"Since Nintendont, DIOS MIOS is generally not used anymore.\n"
"\n"
"                                                                              DIOS MIOS is a tool which allows you to run Gamecube games from a USB.\n"
"\n"
"                                                                              Games must be in discex format, use discex or ModMii's Game Bulk Extractor.", None));
#endif // QT_CONFIG(tooltip)
        self.cmiosList.setSortingEnabled(__sortingEnabled7)

        self.ciosWarning.setText(QCoreApplication.translate("mainWindow", u"Unrecommended cIOSs are intended for compatibility testing or unique situations", None))
        self.ciosNote.setText(QCoreApplication.translate("mainWindow", u"The number in brackets indicates the base IOS; e.g. cIOS222 [**38**] is an IOS installed to slot 222 based on IOS**38**", None))
        self.d2xSettings.setText(QCoreApplication.translate("mainWindow", u"d2x Version\n"
"Settings", None))
        self.wiiRecommended.setText(QCoreApplication.translate("mainWindow", u"Select Recommended", None))
        self.vwiiRecommended.setText(QCoreApplication.translate("mainWindow", u"Select Recommended\n"
"(vWii)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cios), QCoreApplication.translate("mainWindow", u"cIOSs && cMIOSs", None))
        self.pc.setTitle(QCoreApplication.translate("mainWindow", u"PC Programs", None))
        self.wiiu.setTitle(QCoreApplication.translate("mainWindow", u"Wii U Homebrew", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.misc), QCoreApplication.translate("mainWindow", u"WiiU Homebrew && PC Programs ", None))
        self.warning.setText(QCoreApplication.translate("mainWindow", u"Some of these files *_MAY CAUSE BRICK_* if you do not know what you are doing!", None))
        self.download.setText(QCoreApplication.translate("mainWindow", u"Download", None))
    # retranslateUi

