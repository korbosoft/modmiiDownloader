# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
import rc_resource

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
        icon.addFile(u":/base/icon", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.channelList = QListView(self.channels)
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
        self.contentList = QListView(self.contents)
        self.contentList.setObjectName(u"contentList")
        self.contentList.setGeometry(QRect(0, 21, 263, 316))
        sizePolicy.setHeightForWidth(self.contentList.sizePolicy().hasHeightForWidth())
        self.contentList.setSizePolicy(sizePolicy)
        self.contentList.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.contentList.setAlternatingRowColors(True)
        self.contentList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.contentList.setUniformItemSizes(False)

        self.nusLayout.addWidget(self.contents, 1, 0, 1, 1)

        self.realsigned = QGroupBox(self.gridLayoutWidget)
        self.realsigned.setObjectName(u"realsigned")
        sizePolicy1.setHeightForWidth(self.realsigned.sizePolicy().hasHeightForWidth())
        self.realsigned.setSizePolicy(sizePolicy1)
        self.realsigned.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.realsignedList = QListView(self.realsigned)
        self.realsignedList.setObjectName(u"realsignedList")
        self.realsignedList.setGeometry(QRect(0, 21, 262, 316))
        sizePolicy.setHeightForWidth(self.realsignedList.sizePolicy().hasHeightForWidth())
        self.realsignedList.setSizePolicy(sizePolicy)
        self.realsignedList.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.realsignedList.setAlternatingRowColors(True)
        self.realsignedList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.realsignedList.setUniformItemSizes(False)

        self.nusLayout.addWidget(self.realsigned, 0, 1, 1, 1)

        self.other = QGroupBox(self.gridLayoutWidget)
        self.other.setObjectName(u"other")
        sizePolicy1.setHeightForWidth(self.other.sizePolicy().hasHeightForWidth())
        self.other.setSizePolicy(sizePolicy1)
        self.other.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.otherList = QListView(self.other)
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
        self.fakesignedList = QListView(self.fakesigned)
        self.fakesignedList.setObjectName(u"fakesignedList")
        self.fakesignedList.setGeometry(QRect(0, 21, 263, 316))
        sizePolicy.setHeightForWidth(self.fakesignedList.sizePolicy().hasHeightForWidth())
        self.fakesignedList.setSizePolicy(sizePolicy)
        self.fakesignedList.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fakesignedList.setAlternatingRowColors(True)
        self.fakesignedList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.fakesignedList.setUniformItemSizes(False)

        self.nusLayout.addWidget(self.fakesigned, 0, 2, 1, 1)

        self.sysmenus = QGroupBox(self.gridLayoutWidget)
        self.sysmenus.setObjectName(u"sysmenus")
        sizePolicy1.setHeightForWidth(self.sysmenus.sizePolicy().hasHeightForWidth())
        self.sysmenus.setSizePolicy(sizePolicy1)
        self.sysmenus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sysmenuList = QListView(self.sysmenus)
        self.sysmenuList.setObjectName(u"sysmenuList")
        self.sysmenuList.setGeometry(QRect(0, 21, 263, 316))
        sizePolicy.setHeightForWidth(self.sysmenuList.sizePolicy().hasHeightForWidth())
        self.sysmenuList.setSizePolicy(sizePolicy)
        self.sysmenuList.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
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

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"ModMii", None))
        self.channels.setTitle(QCoreApplication.translate("mainWindow", u"Channels", None))
        self.contents.setTitle(QCoreApplication.translate("mainWindow", u"Content Files", None))
        self.realsigned.setTitle(QCoreApplication.translate("mainWindow", u"Non-Fakesigned IOSs\\MIOS", None))
        self.other.setTitle(QCoreApplication.translate("mainWindow", u"Other WADs", None))
        self.fakesigned.setTitle(QCoreApplication.translate("mainWindow", u"Fakesigned IOSs", None))
        self.sysmenus.setTitle(QCoreApplication.translate("mainWindow", u"System Menus", None))
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

        __sortingEnabled = self.hermesList.isSortingEnabled()
        self.hermesList.setSortingEnabled(False)
        ___qlistwidgetitem = self.hermesList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5.1 cIOS202 [60]\u2661", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem.setToolTip(QCoreApplication.translate("mainWindow", u"\u2661Semi-Recommended cIOS. It is the ideal cIOS for slot 202 however it is outdated: cIOS202 was used for older versions of some popular emulators.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem1 = self.hermesList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5.1 cIOS222 [38]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem1.setToolTip(QCoreApplication.translate("mainWindow", u"Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem2 = self.hermesList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5.1 cIOS223 [37]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem2.setToolTip(QCoreApplication.translate("mainWindow", u"Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem3 = self.hermesList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5.1 cIOS224 [57]\u2661", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem3.setToolTip(QCoreApplication.translate("mainWindow", u"\u2661Semi-Recommended cIOS. It is the ideal cIOS for slot 224 however it is outdated. Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem4 = self.hermesList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5 cIOS222 [38]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem4.setToolTip(QCoreApplication.translate("mainWindow", u"Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem5 = self.hermesList.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5 cIOS223 [37]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem5.setToolTip(QCoreApplication.translate("mainWindow", u"Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem6 = self.hermesList.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("mainWindow", u"Hermes-v5 cIOS224 [57]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem6.setToolTip(QCoreApplication.translate("mainWindow", u"Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem7 = self.hermesList.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("mainWindow", u"Hermes-v4 cIOS222 [38]\u2661", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem7.setToolTip(QCoreApplication.translate("mainWindow", u"\u2661Semi-Recommended cIOS. It is the ideal cIOS for slot 222 however it is outdated. Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem8 = self.hermesList.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("mainWindow", u"Hermes-v4 cIOS223 [37+38]\u2661", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem8.setToolTip(QCoreApplication.translate("mainWindow", u"\u2661Semi-Recommended cIOS. It is the ideal cIOS for slot 223 and was widely used for compatibility with guitar-hero games however it is outdated. Since d2x, Hermes cIOSs are generally no longer needed.", None));
#endif // QT_CONFIG(tooltip)
        self.hermesList.setSortingEnabled(__sortingEnabled)

        self.d2x.setTitle(QCoreApplication.translate("mainWindow", u"d2x-d2xversion cIOSs", None))
        self.cmios.setTitle(QCoreApplication.translate("mainWindow", u"cMIOSs", None))

        __sortingEnabled1 = self.cmiosList.isSortingEnabled()
        self.cmiosList.setSortingEnabled(False)
        ___qlistwidgetitem9 = self.cmiosList.item(0)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("mainWindow", u"Swiss cMIOS r1788 [10]\u2661", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem9.setToolTip(QCoreApplication.translate("mainWindow", u"Semi-Recommended cMIOS. A cMIOS with Swiss r1788 built-in. Hold Y during any GameCube mode load to start the built-in Swiss.  If Y is not held, then it should behave identically to WiiGator\\WiiPower's cMIOS and official MIOS. While this is the ideal cMIOS, because of Nintendont, cMIOSs are generally not needed, unless loading backup Gamecube discs on older compatible Wiis.\n"
"\n"
"                                                                              Based on MIOSv10.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem10 = self.cmiosList.item(1)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("mainWindow", u"WiiGator\\Power cMIOS-v0.2 [10]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem10.setToolTip(QCoreApplication.translate("mainWindow", u"Since Nintendont, cMIOSs are generally not needed, unless loading backup Gamecube discs on older compatible Wiis.\n"
"\n"
"                                                                              Based on MIOSv10.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem11 = self.cmiosList.item(2)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("mainWindow", u"WiiGator cMIOS-v0.2 [4]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem11.setToolTip(QCoreApplication.translate("mainWindow", u"Since Nintendont, cMIOSs are generally not needed, unless loading backup Gamecube discs on older compatible Wiis.\n"
"\n"
"                                                                              Based on MIOSv4.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem12 = self.cmiosList.item(3)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("mainWindow", u"Waninkoko cMIOS-rev5 [4]", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem12.setToolTip(QCoreApplication.translate("mainWindow", u"Since Nintendont, cMIOSs are generally not needed, unless loading backup Gamecube discs on older compatible Wiis.\n"
"\n"
"                                                                              Based on MIOSv4.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem13 = self.cmiosList.item(4)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("mainWindow", u"DIOS MIOS Lite (DML) v2.11", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem13.setToolTip(QCoreApplication.translate("mainWindow", u"Since Nintendont, DML is generally not used anymore.\n"
"\n"
"                                                                              DML (Dios Mios Lite) is a tool which allows you to run Gamecube games from an SD Card.\n"
"\n"
"                                                                              Note: for DML to work with SNEEK+DI the WAD must be installed to real NAND and accessed via an emulated NAND.\n"
"\n"
"                                                                              Games must be in discex format, use discex or ModMii's Game Bulk Extractor.", None));
#endif // QT_CONFIG(tooltip)
        ___qlistwidgetitem14 = self.cmiosList.item(5)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("mainWindow", u"DIOS MIOS v2.11", None));
#if QT_CONFIG(tooltip)
        ___qlistwidgetitem14.setToolTip(QCoreApplication.translate("mainWindow", u"Since Nintendont, DIOS MIOS is generally not used anymore.\n"
"\n"
"                                                                              DIOS MIOS is a tool which allows you to run Gamecube games from a USB.\n"
"\n"
"                                                                              Games must be in discex format, use discex or ModMii's Game Bulk Extractor.", None));
#endif // QT_CONFIG(tooltip)
        self.cmiosList.setSortingEnabled(__sortingEnabled1)

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

