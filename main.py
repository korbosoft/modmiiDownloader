# This Python file uses the following encoding: utf-8
import json, os, sys

from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtCore import QEvent

from itertools import chain

from downloadWidgets import DownloadableItem, DownloadListSection

from ciosWidgets import CiosGroupBox

from SearchDialog import SearchDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_mainWindow import Ui_mainWindow

import resources

class mainWindow(QMainWindow):
    enterD2xSettings = False
    queueStr = None

    ui = Ui_mainWindow()

    sections = [
        ['nus', 'sysmenus'],
        ['nus', 'realsigned'],
        ['nus', 'fakesigned'],
        ['nus', 'content'],
        ['nus', 'channels'],
        ['nus', 'other'],
        ['wiiHaxx', 'exploits'],
        ['wiiHaxx', 'wiiHomebrew'],
        ['wiiHaxx', 'vWiiHomebrew'],
        ['wiiHaxx', 'bothHomebrew'],
        ['wiiHaxx', 'hbc'],
        ['cios', 'hermes'],
        ['cios', 'cmios'],
        ['misc', 'pc'],
        ['misc', 'wiiuHomebrew']
    ]

    def setupList(self, page, cat, list):
        for i in self.json['downloadList'][page][cat]['item']:
            index = list.model().rowCount()
            list.model().appendRow(DownloadableItem(i['name']))
            list.model().item(index).setAttrs(i, page, cat)

    def makeQueue(self):
        queue = \
        ''.join([item.getSelected() for item in chain(self.findChildren(DownloadListSection))]) + \
        ''.join([item.getSelected() for item in chain(self.findChildren(CiosGroupBox))]) + \
        self.ui.themeGrid.getSelected() + \
        f'set effect={self.ui.channelEffect.currentText()}\n'
        return queue

    def getQueue(self, str):
        queue = {}
        for line in str.replace('set ', '').splitlines():
            if '=' in line:
                key, value, *_ = line.split('=')
                queue[key] = value
        if 'effect' in queue:
            if queue['effect'] != '':
                self.ui.channelEffect.setCurrentIndex(self.ui.channelEffect.findText(queue['effect']))
        if 'nextpage' in queue:
            if queue['nextpage'].isdigit():
                self.ui.tabWidget.setCurrentIndex(int(queue['nextpage']) - 1)

        queue = [key for key, value in queue.items() if (value == '*' or key == 'No-Spin' or key == 'Spin' or key == 'Fast-Spin')]
        for key in queue:
            for item in self.findChildren(DownloadListSection):
                item.selectChild(key)
            for item in self.findChildren(CiosGroupBox):
                item.selectChild(key)
            self.ui.themeGrid.selectChild(key)

    def setQueue(self):
        exit = False
        for i in self.json['paths']['tempcheck']:
            print(f'Attempting to write to "{i}"')
            try:
                with open(i, 'w') as f:
                    string = self.makeQueue()
                    if self.enterD2xSettings:
                        string = string + 'set nextgoto=betaswitch\nset nextpage=4'
                    f.write(string)
                    print('Success! Exiting now...')
                    exit = True
                    break
            except Exception as e:
                print(f'{type(e).__name__} occurred trying to save queue at "{i}":\n{e}')
        if exit: QApplication.quit()

    def closeEvent(self, event):
        self.setQueue()

    def doD2xSettings(self):
        self.enterD2xSettings = True
        self.setQueue()

    def startSearch(self):
        dialog = SearchDialog()
        dialog.exec()

    def setupAll(self):
        resources.setupIcons()

        self.setupList('nus', 'sysmenus', self.ui.sysmenus.list)
        self.setupList('nus', 'realsigned', self.ui.realsigned.list)
        self.setupList('nus', 'fakesigned', self.ui.fakesigned.list)
        self.setupList('nus', 'content', self.ui.contents.list)
        self.setupList('nus', 'channels', self.ui.channels.list)
        self.setupList('nus', 'other', self.ui.other.list)
        self.setupList('wiiHaxx', 'exploits', self.ui.exploits.list)
        self.setupList('wiiHaxx', 'wiiHomebrew', self.ui.wiiHomebrew.list)
        self.setupList('wiiHaxx', 'vWiiHomebrew', self.ui.vWiiHomebrew.list)
        self.setupList('wiiHaxx', 'bothHomebrew', self.ui.bothHomebrew.list)
        self.setupList('wiiHaxx', 'hbc', self.ui.hbc.list)
        self.setupList('cios', 'hermes', self.ui.hermes.list)
        self.setupList('cios', 'cmios', self.ui.cmios.list)
        self.setupList('misc', 'pc', self.ui.pc.list)
        self.setupList('misc', 'wiiuHomebrew', self.ui.wiiuHomebrew.list)

        # Page 1
        self.ui.tabWidget.setTabIcon(0, resources.icons['nus_24'])

        # Page 2
        self.ui.tabWidget.setTabIcon(1, resources.icons['program_24'])

        # Page 3
        self.ui.tabWidget.setTabIcon(2, resources.icons['theme_24'])

        # Page 4
        self.ui.tabWidget.setTabIcon(3, resources.icons['ios_24'])
        self.ui.d2x.setup(self.json['paths'], self.json['recommendedWiiCios'])
        self.ui.d2xSettings.clicked.connect(self.doD2xSettings)
        self.ui.wiiRecommended.setIcon(resources.icons['recommended_24'])
        self.ui.vWiiRecommended.setIcon(resources.icons['recommended_24'])
        self.ui.wiiRecommended.clicked.connect(self.ui.d2x.toggleWiiRecommended)
        self.ui.vWiiRecommended.clicked.connect(self.ui.d2x.toggleVWiiRecommended)

        # Page 5
        self.ui.tabWidget.setTabIcon(4, resources.icons['program_24'])
        self.ui.download.setIcon(resources.icons['download_24'])
        self.ui.download.clicked.connect(self.close)
        self.ui.search.setIcon(resources.icons['search_24'])
        self.ui.search.clicked.connect(self.startSearch)
        self.ui.legendIcon1.setPixmap(resources.icons['recommended_24'].pixmap(24))
        self.ui.legendIcon2.setPixmap(resources.icons['semiRecommended_24'].pixmap(24))
        self.ui.legendIcon3.setPixmap(resources.icons['update_24'].pixmap(24))
        self.ui.legendIcon4.setPixmap(resources.icons['semiAutoUpdate_24'].pixmap(24))

    def setStatus(self):
        count = self.makeQueue().count('*')
        if count == 1:
            self.statusBar().showMessage('1 item selected')
        self.statusBar().showMessage(f'{count} items selected')

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.UpdateRequest:
            self.setStatus()
            return False

        return super().eventFilter(obj, event)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        try:
            with open('Support/subscripts/ModMiiDownloader/downloader.json') as f:
                j = json.load(f)
        except:
            with open('downloader.json') as f:
                j = json.load(f)
        self.json = j
        self.setupAll()
        self.setStatus()
        self.statusBar().setSizeGripEnabled(False)
        self.installEventFilter(self)
        for i in self.json['paths']['input']:
            print(f'Attempting to load "{i}"')
            try:
                with open(i) as f:
                    self.queueStr = f.read()
            except FileNotFoundError:
                print(f'No queue at "{i}"')
            except Exception as e:
                print(f'{type(e).__name__} occurred trying to load queue at "{i}":\n{e}')
        if self.queueStr is not None:
            self.getQueue(self.queueStr)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = mainWindow()
    widget.show()
    try:
        with open('temp/wineactive.txt', 'w') as f:
            pass
    except:
        with open('wineactive.txt', 'w') as f:
            pass
    ret = app.exec()
    try:
        os.remove('temp/wineactive.txt')
    except:
        os.remove('wineactive.txt')
    sys.exit(ret)
