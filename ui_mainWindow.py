# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QWidget)

from ThemeGrid import ThemeGrid
from ciosWidgets import (D2xCheckGrid, WaninCheckGrid)
from downloadWidgets import DownloadListSection
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
        icon.addFile(u":/base/mainIcon", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 800, 721))
        self.tabWidget.setDocumentMode(True)
        self.nus = QWidget()
        self.nus.setObjectName(u"nus")
        self.nusLayout = QWidget(self.nus)
        self.nusLayout.setObjectName(u"nusLayout")
        self.nusLayout.setGeometry(QRect(0, 0, 800, 688))
        self.nusLayout1 = QGridLayout(self.nusLayout)
        self.nusLayout1.setObjectName(u"nusLayout1")
        self.nusLayout1.setContentsMargins(0, 0, 0, 0)
        self.sysmenus = DownloadListSection(self.nusLayout)
        self.sysmenus.setObjectName(u"sysmenus")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sysmenus.sizePolicy().hasHeightForWidth())
        self.sysmenus.setSizePolicy(sizePolicy1)
        self.sysmenus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nusLayout1.addWidget(self.sysmenus, 0, 0, 1, 1)

        self.realsigned = DownloadListSection(self.nusLayout)
        self.realsigned.setObjectName(u"realsigned")
        sizePolicy1.setHeightForWidth(self.realsigned.sizePolicy().hasHeightForWidth())
        self.realsigned.setSizePolicy(sizePolicy1)
        self.realsigned.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nusLayout1.addWidget(self.realsigned, 0, 1, 1, 1)

        self.fakesigned = DownloadListSection(self.nusLayout)
        self.fakesigned.setObjectName(u"fakesigned")
        sizePolicy1.setHeightForWidth(self.fakesigned.sizePolicy().hasHeightForWidth())
        self.fakesigned.setSizePolicy(sizePolicy1)
        self.fakesigned.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nusLayout1.addWidget(self.fakesigned, 0, 2, 1, 1)

        self.contents = DownloadListSection(self.nusLayout)
        self.contents.setObjectName(u"contents")
        sizePolicy1.setHeightForWidth(self.contents.sizePolicy().hasHeightForWidth())
        self.contents.setSizePolicy(sizePolicy1)
        self.contents.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nusLayout1.addWidget(self.contents, 1, 0, 1, 1)

        self.channels = DownloadListSection(self.nusLayout)
        self.channels.setObjectName(u"channels")
        sizePolicy1.setHeightForWidth(self.channels.sizePolicy().hasHeightForWidth())
        self.channels.setSizePolicy(sizePolicy1)
        self.channels.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nusLayout1.addWidget(self.channels, 1, 1, 1, 1)

        self.other = DownloadListSection(self.nusLayout)
        self.other.setObjectName(u"other")
        sizePolicy1.setHeightForWidth(self.other.sizePolicy().hasHeightForWidth())
        self.other.setSizePolicy(sizePolicy1)
        self.other.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nusLayout1.addWidget(self.other, 1, 2, 1, 1)

        self.fakesigned.raise_()
        self.channels.raise_()
        self.other.raise_()
        self.sysmenus.raise_()
        self.realsigned.raise_()
        self.contents.raise_()
        icon1 = QIcon()
        icon1.addFile(u":/base/svg_nus", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.nus, icon1, "")
        self.homebrew = QWidget()
        self.homebrew.setObjectName(u"homebrew")
        self.wiiLayout = QWidget(self.homebrew)
        self.wiiLayout.setObjectName(u"wiiLayout")
        self.wiiLayout.setGeometry(QRect(0, 0, 800, 688))
        self.wiiLayout1 = QGridLayout(self.wiiLayout)
        self.wiiLayout1.setObjectName(u"wiiLayout1")
        self.wiiLayout1.setContentsMargins(0, 0, 0, 0)
        self.hbc = DownloadListSection(self.wiiLayout)
        self.hbc.setObjectName(u"hbc")
        sizePolicy1.setHeightForWidth(self.hbc.sizePolicy().hasHeightForWidth())
        self.hbc.setSizePolicy(sizePolicy1)
        self.hbc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wiiLayout1.addWidget(self.hbc, 1, 0, 1, 1)

        self.vWiiHomebrew = DownloadListSection(self.wiiLayout)
        self.vWiiHomebrew.setObjectName(u"vWiiHomebrew")
        sizePolicy1.setHeightForWidth(self.vWiiHomebrew.sizePolicy().hasHeightForWidth())
        self.vWiiHomebrew.setSizePolicy(sizePolicy1)
        self.vWiiHomebrew.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wiiLayout1.addWidget(self.vWiiHomebrew, 1, 1, 1, 1)

        self.wiiHomebrew = DownloadListSection(self.wiiLayout)
        self.wiiHomebrew.setObjectName(u"wiiHomebrew")
        sizePolicy1.setHeightForWidth(self.wiiHomebrew.sizePolicy().hasHeightForWidth())
        self.wiiHomebrew.setSizePolicy(sizePolicy1)
        self.wiiHomebrew.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wiiLayout1.addWidget(self.wiiHomebrew, 0, 1, 1, 1)

        self.bothHomebrew = DownloadListSection(self.wiiLayout)
        self.bothHomebrew.setObjectName(u"bothHomebrew")
        sizePolicy1.setHeightForWidth(self.bothHomebrew.sizePolicy().hasHeightForWidth())
        self.bothHomebrew.setSizePolicy(sizePolicy1)
        self.bothHomebrew.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wiiLayout1.addWidget(self.bothHomebrew, 0, 2, 2, 1)

        self.exploits = DownloadListSection(self.wiiLayout)
        self.exploits.setObjectName(u"exploits")
        sizePolicy1.setHeightForWidth(self.exploits.sizePolicy().hasHeightForWidth())
        self.exploits.setSizePolicy(sizePolicy1)
        self.exploits.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wiiLayout1.addWidget(self.exploits, 0, 0, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u":/base/svg_program", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.homebrew, icon2, "")
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
        self.themeGrid = ThemeGrid(self.themes)
        self.themeGrid.setObjectName(u"themeGrid")
        self.themeGrid.setGeometry(QRect(0, 0, 800, 630))
        sizePolicy1.setHeightForWidth(self.themeGrid.sizePolicy().hasHeightForWidth())
        self.themeGrid.setSizePolicy(sizePolicy1)
        self.channelEffect = QComboBox(self.themes)
        self.channelEffect.addItem("")
        self.channelEffect.addItem("")
        self.channelEffect.addItem("")
        self.channelEffect.setObjectName(u"channelEffect")
        self.channelEffect.setGeometry(QRect(690, 660, 110, 30))
        self.channelEffectLabel = QLabel(self.themes)
        self.channelEffectLabel.setObjectName(u"channelEffectLabel")
        self.channelEffectLabel.setGeometry(QRect(590, 660, 100, 30))
        icon3 = QIcon()
        icon3.addFile(u":/base/svg_theme", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.themes, icon3, "")
        self.cios = QWidget()
        self.cios.setObjectName(u"cios")
        self.ciosLayout = QWidget(self.cios)
        self.ciosLayout.setObjectName(u"ciosLayout")
        self.ciosLayout.setGeometry(QRect(0, 0, 800, 640))
        self.ciosLayout1 = QGridLayout(self.ciosLayout)
        self.ciosLayout1.setObjectName(u"ciosLayout1")
        self.ciosLayout1.setContentsMargins(0, 0, 0, 0)
        self.hermes = DownloadListSection(self.ciosLayout)
        self.hermes.setObjectName(u"hermes")
        self.hermes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ciosLayout1.addWidget(self.hermes, 0, 2, 1, 1)

        self.wanin = WaninCheckGrid(self.ciosLayout)
        self.wanin.setObjectName(u"wanin")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.wanin.sizePolicy().hasHeightForWidth())
        self.wanin.setSizePolicy(sizePolicy2)
        self.wanin.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ciosLayout1.addWidget(self.wanin, 0, 1, 2, 1)

        self.d2x = D2xCheckGrid(self.ciosLayout)
        self.d2x.setObjectName(u"d2x")
        self.d2x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ciosLayout1.addWidget(self.d2x, 0, 0, 2, 1)

        self.cmios = DownloadListSection(self.ciosLayout)
        self.cmios.setObjectName(u"cmios")
        self.cmios.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ciosLayout1.addWidget(self.cmios, 1, 2, 1, 1)

        self.ciosWarning = QLabel(self.cios)
        self.ciosWarning.setObjectName(u"ciosWarning")
        self.ciosWarning.setGeometry(QRect(585, 640, 215, 50))
        font1 = QFont()
        font1.setBold(True)
        self.ciosWarning.setFont(font1)
        self.ciosWarning.setTextFormat(Qt.TextFormat.PlainText)
        self.ciosWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ciosWarning.setWordWrap(True)
        self.ciosWarning.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.d2xSettings = QPushButton(self.cios)
        self.d2xSettings.setObjectName(u"d2xSettings")
        self.d2xSettings.setGeometry(QRect(0, 640, 90, 50))
        self.d2xSettings.setIconSize(QSize(24, 24))
        self.wiiRecommended = QPushButton(self.cios)
        self.wiiRecommended.setObjectName(u"wiiRecommended")
        self.wiiRecommended.setGeometry(QRect(235, 640, 170, 50))
        icon4 = QIcon()
        icon4.addFile(u":/base/svg_recommended", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.wiiRecommended.setIcon(icon4)
        self.wiiRecommended.setIconSize(QSize(24, 24))
        self.vWiiRecommended = QPushButton(self.cios)
        self.vWiiRecommended.setObjectName(u"vWiiRecommended")
        self.vWiiRecommended.setGeometry(QRect(405, 640, 180, 50))
        self.vWiiRecommended.setIcon(icon4)
        self.vWiiRecommended.setIconSize(QSize(24, 24))
        self.ciosInfo = QLabel(self.cios)
        self.ciosInfo.setObjectName(u"ciosInfo")
        self.ciosInfo.setGeometry(QRect(90, 640, 145, 50))
        self.ciosInfo.setFont(font1)
        self.ciosInfo.setTextFormat(Qt.TextFormat.PlainText)
        self.ciosInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ciosInfo.setWordWrap(True)
        self.ciosInfo.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        icon5 = QIcon()
        icon5.addFile(u":/base/svg_ios", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.cios, icon5, "")
        self.misc = QWidget()
        self.misc.setObjectName(u"misc")
        self.wiiuLayout = QWidget(self.misc)
        self.wiiuLayout.setObjectName(u"wiiuLayout")
        self.wiiuLayout.setGeometry(QRect(0, 0, 800, 688))
        self.wiiuLayout1 = QGridLayout(self.wiiuLayout)
        self.wiiuLayout1.setObjectName(u"wiiuLayout1")
        self.wiiuLayout1.setContentsMargins(0, 0, 0, 0)
        self.pc = DownloadListSection(self.wiiuLayout)
        self.pc.setObjectName(u"pc")
        sizePolicy1.setHeightForWidth(self.pc.sizePolicy().hasHeightForWidth())
        self.pc.setSizePolicy(sizePolicy1)
        self.pc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wiiuLayout1.addWidget(self.pc, 0, 1, 1, 1)

        self.wiiuHomebrew = DownloadListSection(self.wiiuLayout)
        self.wiiuHomebrew.setObjectName(u"wiiuHomebrew")
        sizePolicy1.setHeightForWidth(self.wiiuHomebrew.sizePolicy().hasHeightForWidth())
        self.wiiuHomebrew.setSizePolicy(sizePolicy1)
        self.wiiuHomebrew.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wiiuLayout1.addWidget(self.wiiuHomebrew, 0, 0, 1, 1)

        self.tabWidget.addTab(self.misc, icon2, "")
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
        icon6 = QIcon()
        icon6.addFile(u":/base/svg_download", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.download.setIcon(icon6)
        self.download.setIconSize(QSize(24, 24))
        self.legendLayout = QWidget(self.centralwidget)
        self.legendLayout.setObjectName(u"legendLayout")
        self.legendLayout.setGeometry(QRect(290, 720, 400, 50))
        self.legendLayout1 = QGridLayout(self.legendLayout)
        self.legendLayout1.setObjectName(u"legendLayout1")
        self.legendLayout1.setContentsMargins(0, 0, 0, 0)
        self.legendLabel1 = QLabel(self.legendLayout)
        self.legendLabel1.setObjectName(u"legendLabel1")

        self.legendLayout1.addWidget(self.legendLabel1, 0, 2, 1, 1)

        self.legendIcon1 = QLabel(self.legendLayout)
        self.legendIcon1.setObjectName(u"legendIcon1")

        self.legendLayout1.addWidget(self.legendIcon1, 0, 1, 1, 1)

        self.legendSpacer5 = QSpacerItem(0, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.legendLayout1.addItem(self.legendSpacer5, 0, 0, 2, 1)

        self.legendIcon2 = QLabel(self.legendLayout)
        self.legendIcon2.setObjectName(u"legendIcon2")

        self.legendLayout1.addWidget(self.legendIcon2, 1, 1, 1, 1)

        self.legendLabel2 = QLabel(self.legendLayout)
        self.legendLabel2.setObjectName(u"legendLabel2")

        self.legendLayout1.addWidget(self.legendLabel2, 1, 2, 1, 1)

        self.legendSpacer4 = QSpacerItem(0, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.legendLayout1.addItem(self.legendSpacer4, 0, 3, 2, 1)

        self.legendLabel3 = QLabel(self.legendLayout)
        self.legendLabel3.setObjectName(u"legendLabel3")

        self.legendLayout1.addWidget(self.legendLabel3, 0, 5, 1, 1)

        self.legendIcon3 = QLabel(self.legendLayout)
        self.legendIcon3.setObjectName(u"legendIcon3")

        self.legendLayout1.addWidget(self.legendIcon3, 0, 4, 1, 1)

        self.legendIcon4 = QLabel(self.legendLayout)
        self.legendIcon4.setObjectName(u"legendIcon4")

        self.legendLayout1.addWidget(self.legendIcon4, 1, 4, 1, 1)

        self.legendLabel4 = QLabel(self.legendLayout)
        self.legendLabel4.setObjectName(u"legendLabel4")

        self.legendLayout1.addWidget(self.legendLabel4, 1, 5, 1, 1)

        self.legendSpacer6 = QSpacerItem(0, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.legendLayout1.addItem(self.legendSpacer6, 0, 6, 2, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(mainWindow)
        self.statusBar.setObjectName(u"statusBar")
        mainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.tabWidget, self.wiiRecommended)
        QWidget.setTabOrder(self.wiiRecommended, self.vWiiRecommended)
        QWidget.setTabOrder(self.vWiiRecommended, self.d2xSettings)
        QWidget.setTabOrder(self.d2xSettings, self.download)

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"ModMii", None))
        self.sysmenus.setTitle(QCoreApplication.translate("mainWindow", u"System Menus", None))
        self.realsigned.setTitle(QCoreApplication.translate("mainWindow", u"Non-Fakesigned IOSs\\MIOS", None))
        self.fakesigned.setTitle(QCoreApplication.translate("mainWindow", u"Fakesigned IOSs", None))
        self.contents.setTitle(QCoreApplication.translate("mainWindow", u"Content Files", None))
        self.channels.setTitle(QCoreApplication.translate("mainWindow", u"Channels", None))
        self.other.setTitle(QCoreApplication.translate("mainWindow", u"Other WADs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.nus), QCoreApplication.translate("mainWindow", u"NUS Files", None))
        self.hbc.setTitle(QCoreApplication.translate("mainWindow", u"Homebrew Channels", None))
        self.vWiiHomebrew.setTitle(QCoreApplication.translate("mainWindow", u"vWii Only Homebrew", None))
        self.wiiHomebrew.setTitle(QCoreApplication.translate("mainWindow", u"Wii-Only Homebrew", None))
        self.bothHomebrew.setTitle(QCoreApplication.translate("mainWindow", u"(v)Wii Homebrew", None))
        self.exploits.setTitle(QCoreApplication.translate("mainWindow", u"Exploits", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homebrew), QCoreApplication.translate("mainWindow", u"(v)Wii Homebrew && Exploits", None))
        self.themeProtectWarning.setText(QCoreApplication.translate("mainWindow", u" DON'T INSTALL THEMES WITHOUT PROTECTION: _BOOTMII, PRIILOADER AND NAND BACKUP_", None))
        self.themeSysmenuWarning.setText(QCoreApplication.translate("mainWindow", u"ONLY INSTALL THEMES FOR _YOUR SPECIFIC SYSTEM MENU VERSION AND REGION!_", None))
        self.channelEffect.setItemText(0, QCoreApplication.translate("mainWindow", u"No-Spin", None))
        self.channelEffect.setItemText(1, QCoreApplication.translate("mainWindow", u"Spin", None))
        self.channelEffect.setItemText(2, QCoreApplication.translate("mainWindow", u"Fast-Spin", None))

        self.channelEffectLabel.setText(QCoreApplication.translate("mainWindow", u"Channel Effect:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.themes), QCoreApplication.translate("mainWindow", u"System Menu Themes", None))
        self.hermes.setTitle(QCoreApplication.translate("mainWindow", u"Hermes cIOSs", None))
        self.wanin.setTitle(QCoreApplication.translate("mainWindow", u"Waninkoko cIOSs", None))
        self.d2x.setTitle(QCoreApplication.translate("mainWindow", u"d2x-d2xversion cIOSs", None))
        self.cmios.setTitle(QCoreApplication.translate("mainWindow", u"cMIOSs", None))
        self.ciosWarning.setText(QCoreApplication.translate("mainWindow", u"Unrecommended cIOSs are intended for compatibility testing or unique situations", None))
        self.d2xSettings.setText(QCoreApplication.translate("mainWindow", u"d2x Version\n"
"Settings", None))
        self.wiiRecommended.setText(QCoreApplication.translate("mainWindow", u"Select Recommended", None))
        self.vWiiRecommended.setText(QCoreApplication.translate("mainWindow", u"Select Recommended\n"
"(vWii)", None))
        self.ciosInfo.setText(QCoreApplication.translate("mainWindow", u"e.g., cIOS249 [56] = cIOS at slot 249 based on IOS56", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cios), QCoreApplication.translate("mainWindow", u"cIOSs && cMIOSs", None))
        self.pc.setTitle(QCoreApplication.translate("mainWindow", u"PC Programs", None))
        self.wiiuHomebrew.setTitle(QCoreApplication.translate("mainWindow", u"Wii U Homebrew", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.misc), QCoreApplication.translate("mainWindow", u"Wii U Homebrew && PC Programs ", None))
        self.warning.setText(QCoreApplication.translate("mainWindow", u"Some of these files *_MAY CAUSE BRICK_* if you do not know what you are doing!", None))
        self.download.setText(QCoreApplication.translate("mainWindow", u"Download", None))
        self.legendLabel1.setText(QCoreApplication.translate("mainWindow", u"Recommended", None))
        self.legendLabel2.setText(QCoreApplication.translate("mainWindow", u"Semi-Recommended", None))
        self.legendLabel3.setText(QCoreApplication.translate("mainWindow", u"Auto-Updating", None))
        self.legendLabel4.setText(QCoreApplication.translate("mainWindow", u"Updated when XFlak Remembers", None))
    # retranslateUi

