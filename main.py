# This Python file uses the following encoding: utf-8

import os, sys

from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtCore import QEvent

from itertools import chain

from downloadWidgets import DownloadableItem, DownloadListSection

from ciosWidgets import CiosGroupBox

from searchWidgets import SearchDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_MainWindow import Ui_MainWindow

import resources

from config import config

class mainWindow(QMainWindow):
    enterD2xSettings = False
    queueStr = None
    d2xRev = None

    ui = Ui_MainWindow()

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

    def setupList(self, page, cat, item_list):
        for i in config['downloadList'][page][cat]['item']:
            index = item_list.model().rowCount()
            item_list.model().appendRow(DownloadableItem(i['name']))
            item_list.model().item(index).setAttrs(i, page, cat)

    def makeQueue(self):
        queue = \
        ''.join([item.getSelected() for item in chain(self.findChildren(DownloadListSection))]) + \
        ''.join([item.getSelected() for item in chain(self.findChildren(CiosGroupBox))]) + \
        self.ui.themeGrid.getSelected() + \
        f'set effect={self.ui.channelEffect.currentText()}\n' + \
        f'set nextpage={self.ui.tabWidget.currentIndex() + 1}\n'
        return queue

    def getQueue(self, string):
        queue = {}
        for line in string.replace('set ', '').splitlines():
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
        for i in config['paths']['tempcheck']:
            print(f'Attempting to write to "{i}"')
            try:
                with open(i, 'w') as f:
                    string = self.makeQueue()
                    if self.enterD2xSettings:
                        string = string + 'set nextgoto=betaswitch\n'
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

        self.setupList('nus', 'sysmenus', self.ui.sysmenus.item_list)
        self.setupList('nus', 'realsigned', self.ui.realsigned.item_list)
        self.setupList('nus', 'fakesigned', self.ui.fakesigned.item_list)
        self.setupList('nus', 'content', self.ui.content.item_list)
        self.setupList('nus', 'channels', self.ui.channels.item_list)
        self.setupList('nus', 'other', self.ui.other.item_list)
        self.setupList('wiiHaxx', 'exploits', self.ui.exploits.item_list)
        self.setupList('wiiHaxx', 'wiiHomebrew', self.ui.wiiHomebrew.item_list)
        self.setupList('wiiHaxx', 'vWiiHomebrew', self.ui.vWiiHomebrew.item_list)
        self.setupList('wiiHaxx', 'bothHomebrew', self.ui.bothHomebrew.item_list)
        self.setupList('wiiHaxx', 'hbc', self.ui.hbc.item_list)
        self.setupList('cios', 'hermes', self.ui.hermes.item_list)
        self.setupList('cios', 'cmios', self.ui.cmios.item_list)
        self.setupList('misc', 'pc', self.ui.pc.item_list)
        self.setupList('misc', 'wiiuHomebrew', self.ui.wiiuHomebrew.item_list)

        # Page 1
        self.ui.tabWidget.setTabIcon(0, resources.icons['1_24'])

        # Page 2
        self.ui.tabWidget.setTabIcon(1, resources.icons['2_24'])

        # Page 3
        self.ui.tabWidget.setTabIcon(2, resources.icons['3_24'])

        # Page 4
        self.ui.tabWidget.setTabIcon(3, resources.icons['4_24'])
        self.ui.d2xSettings.clicked.connect(self.doD2xSettings)
        self.ui.wiiRecommended.setIcon(resources.icons['recommended_24'])
        self.ui.vWiiRecommended.setIcon(resources.icons['recommended_24'])
        self.ui.wiiRecommended.clicked.connect(self.ui.d2x.selectWiiRecommended)
        self.ui.vWiiRecommended.clicked.connect(self.ui.d2x.selectVWiiRecommended)
        self.ui.d2x.setup(self.d2xRev)

        # Page 5
        self.ui.tabWidget.setTabIcon(4, resources.icons['5_24'])
        self.ui.download.setIcon(resources.icons['download_24'])
        self.ui.download.clicked.connect(self.close)
        self.ui.search.setIcon(resources.icons['search_24'])
        self.ui.search.clicked.connect(self.startSearch)
        self.ui.legendIcon1.setPixmap(resources.icons['recommended_24'].pixmap(24))
        self.ui.legendIcon2.setPixmap(resources.icons['semiRecommended_24'].pixmap(24))
        self.ui.legendIcon3.setPixmap(resources.icons['update_24'].pixmap(24))
        self.ui.legendIcon4.setPixmap(resources.icons['semiAutoUpdate_24'].pixmap(24))

    def setStatus(self):
        count = self.makeQueue().count('=*')
        str = ''
        if count == 0:
            str = 'No items '
        elif count == 1:
            str = '1 item '
        else:
            str = f'{count} items '
        str += 'in queue'
        self.statusBar().showMessage(str)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.UpdateRequest:
            self.setStatus()
            return False

        return super().eventFilter(obj, event)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui.setupUi(self)

        for i in config['paths']['tempcheck']:
            print(f'Attempting to load "{i}"')
            try:
                with open(i) as f:
                    self.queueStr = f.read()
            except FileNotFoundError:
                print(f'No vars at "{i}"')
            except Exception as e:
                print(f'{type(e).__name__} occurred trying to load vars at "{i}":\n{e}')

        if self.queueStr is not None:
            queue = {}
            for line in self.queueStr.replace('set ', '').splitlines():
                if '=' in line:
                    key, value, *_ = line.split('=')
                    queue[key] = value
            if 'd2x-beta-rev' in queue and queue['d2x-beta-rev'] != '':
                self.d2xRev = queue['d2x-beta-rev']
            else: self.d2xRev = 'if you are seeing this then korbo forgot to comment a line out'

        self.setFixedSize(self.size())
        self.setupAll()

        if self.queueStr is not None:
            self.getQueue(self.queueStr)

        self.setStatus()
        self.statusBar().setSizeGripEnabled(False)
        self.statusBar().clicked.connect(self.startSearch)
        self.installEventFilter(self)

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
        try:
            os.remove('wineactive.txt')
        except:
            print('"wineactive.txt" not found. Task failed successfully??')
    sys.exit(ret)
