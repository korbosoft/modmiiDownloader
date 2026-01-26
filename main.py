# This Python file uses the following encoding: utf-8
import sys, json

from PySide6.QtWidgets import QApplication, QCheckBox, QLabel, QMainWindow, QWidget

from PySide6.QtCore import QRegularExpression, Slot, QFile

from xml.etree import ElementTree

from DownloadWidgets import DownloadableItem, DownloadList

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_mainWindow import Ui_mainWindow

import resources

class mainWindow(QMainWindow):
    ui = Ui_mainWindow()
    wiiMap = None
    vWiiMap = None

    def setupList(self, page, cat, list):
        for i in self.json['downloadList'][page][cat]['item']:
            index = list.model().rowCount()
            list.model().appendRow(DownloadableItem(i['title']))
            list.model().item(index).setAttrs(i)


    @Slot()
    def doD2xSettings(self):
        print('TODO: actually do this')
        print('objFSO.write vbNewLine & "set nextgoto=" & nextgoto\nobjFSO.write vbNewLine & "set nextpage=" & nextpage')

    def loadD2xMaps(self):
        # load Wii cIOS map
        for i in self.json['paths']['wiiMap']:
            try:
                print(f'Attempting to load "{i}"')
                self.wiiMap = ElementTree.parse(i).getroot()
            except FileNotFoundError as e:
                print(f'There seems to be no cIOS map at {i}:\n{e}')
            except ElementTree.ParseError as e:
                print(f'ParseError occurred trying to parse Wii cIOS map at {i}:\n{e}')
            except Exception as e:
                print(f'{type(e).__name__} occurred trying to load/parse Wii cIOS map at {i}:\n{e}')
        if self.wiiMap is None:
            print('Failed to load/parse ciosmaps.xml, so probably no d2x for you, sorry :(')
        else:
            print('Successfully loaded & parsed ciosmaps.xml!')
        # load vWii cIOS map
        for i in self.json['paths']['vWiiMap']:
            try:
                print(f'Attempting to load "{i}"')
                self.vWiiMap = ElementTree.parse(i).getroot()
            except FileNotFoundError as e:
                print(f'There seems to be no cIOS map at {i}:\n{e}')
            except ElementTree.ParseError as e:
                print(f'ParseError occurred trying to parse vWii cIOS map at {i}:\n{e}')
            except Exception as e:
                print(f'{type(e).__name__} occurred trying to load/parse vWii cIOS map at {i}:\n{e}')
        if self.vWiiMap is None:
            print('Failed to load/parse ciosmaps_vWii.xml, so no vWii d2x. :/')
        else:
            print('Successfully loaded & parsed ciosmaps_vWii.xml!')

    def isIOSBaseAvailable(self, base, map):
        for i in map.find('ciosgroup').findall('base'):
            if i.get('ios') == str(base):
                return True
        return False

    def setupD2x(self):
        self.ui.d2xSettings.clicked.connect(self.doD2xSettings)

        self.loadD2xMaps()

        self.ui.d2x.setTitle(f'{self.wiiMap.find('ciosgroup').get('name')} cIOSs')

        for widget in self.ui.d2x.findChildren(QCheckBox, QRegularExpression('^db')):
            widget.setIcon(resources.icons['blank_24'])
        for widget in self.ui.d2x.findChildren(QCheckBox, QRegularExpression('^dvb')):
            widget.setIcon(resources.icons['recommended_24'])

        for base in [37, 38, 53, 55, 56, 57, 58, 60, 70, 80]:
            enabled = self.isIOSBaseAvailable(base, self.wiiMap)
            for widget in self.ui.d2x.findChildren(QWidget, QRegularExpression(f'^db{base}')):
                widget.setEnabled(enabled)
        if self.vWiiMap is not None:
            for base in [38, 56, 57, 58]:
                self.ui.d2x.findChild(QLabel, 'dv').setEnabled(True)
                enabled = self.isIOSBaseAvailable(base, self.vWiiMap)
                for widget in self.ui.d2x.findChildren(QCheckBox, QRegularExpression(f'^dvb{base}')):
                    widget.setEnabled(enabled)

        for item in self.json['recommendedCios']:
            self.ui.d2x.findChild(QCheckBox, f'db{item['base']}s{item['slot']}').setIcon(resources.icons['recommended_24'])

    def createQueue(self):
        print('FIXME: actually do this')

    def setupAll(self):
        resources.setupIcons()
        # Page 1
        self.setupList('nus', 'sysmenus', self.ui.sysmenus.findChild(DownloadList))
        self.setupList('nus', 'realsigned', self.ui.realsigned.findChild(DownloadList))
        self.setupList('nus', 'fakesigned', self.ui.fakesigned.findChild(DownloadList))
        self.setupList('nus', 'content', self.ui.contents.findChild(DownloadList))
        self.setupList('nus', 'channels', self.ui.channels.findChild(DownloadList))
        self.setupList('nus', 'other', self.ui.other.findChild(DownloadList))
        # Page 2
        self.setupList('wiiHaxx', 'exploits', self.ui.exploits.findChild(DownloadList))
        self.setupList('wiiHaxx', 'wiiHomebrew', self.ui.wiiHomebrew.findChild(DownloadList))
        self.setupList('wiiHaxx', 'vWiiHomebrew', self.ui.vWiiHomebrew.findChild(DownloadList))
        self.setupList('wiiHaxx', 'bothHomebrew', self.ui.bothHomebrew.findChild(DownloadList))
        self.setupList('wiiHaxx', 'hbc', self.ui.hbc.findChild(DownloadList))

        # Page 4
        self.setupD2x()
        self.setupList('cios', 'hermes', self.ui.hermes.findChild(DownloadList))
        self.setupList('cios', 'cmios', self.ui.cmios.findChild(DownloadList))

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui.setupUi(self)
        with open('downloader.json') as f:
            j = json.load(f)
        self.json = j
        self.setupAll()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = mainWindow()
    widget.show()
    sys.exit(app.exec())
