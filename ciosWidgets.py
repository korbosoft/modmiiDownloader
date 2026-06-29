# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QCheckBox, QGroupBox, QLabel

from PySide6.QtCore import QRegularExpression

from xml.etree import ElementTree

from utils import toggleCheckBoxes

import os

import resources

from config import config

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_D2xCheckGrid import Ui_D2xCheckGrid

from ui_WaninCheckGrid import Ui_WaninCheckGrid

class CiosGroupBox(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)

    def getSelected(self):
        str = ''
        for i in self.findChildren(QCheckBox):
            str = str + f'set {i.objectName()}={'*' if i.isEnabled() and i.isChecked() else ''}\n'
        return str

    def selectChild(self, name):
        child = self.findChild(QCheckBox, name)
        if child is not None:
            child.setChecked(True)

    def selectAll(self):
        toggleCheckBoxes(self, self.findChildren(QCheckBox))

    def resizeEvent(self, event):
        self.ui.layout.setGeometry(self.geometry())

class D2xCheckGrid(CiosGroupBox):
    wiiMap = None
    vWiiMap = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_D2xCheckGrid()
        self.ui.setupUi(self)
        self.ui.select.clicked.connect(self.selectAll)

    def setup(self, d2xRev):
        self.loadD2xMaps(d2xRev)
        self.setupD2x()

    def toggleWiiRecommended(self):
        toggleCheckBoxes(self, [self.findChild(QCheckBox, f'c{cios['slot']}_{cios['base']}_d2x') for cios in config['recommendedWiiCios']])

    def toggleVWiiRecommended(self):
        toggleCheckBoxes(self, '_vWii$', True)

    def loadD2xMaps(self, d2xRev):
        # load Wii cIOS map
        for i in range(len(config['paths']['wiiMap'])):
            path = config['paths']['wiiMap'][i]
            try:
                print(f'Attempting to load "{path}"')
                map = ElementTree.parse(path).getroot()
                if map.find('ciosgroup').get('name') == f'd2x-v{d2xRev}':
                    self.wiiMap = map
                break
            except FileNotFoundError:
                print(f'There seems to be no cIOS map at "{path}"')
            except ElementTree.ParseError as e:
                print(f'ParseError occurred trying to parse Wii cIOS map at "{path}":\n{e}')
            except Exception as e:
                print(f'{type(e).__name__} occurred trying to load/parse Wii cIOS map at "{path}":\n{e}')
        if self.wiiMap is None:
            print('Failed to load/parse ciosmaps.xml, so no Wii d2x. This shouldn\'t ever happen?')
        else:
            print('Successfully loaded & parsed ciosmaps.xml!')
        # load vWii cIOS map
        path = config['paths']['vWiiMap'][i]
        try:
            print(f'Attempting to load "{path}"')
            self.vWiiMap = ElementTree.parse(path).getroot()
        except FileNotFoundError:
            print(f'There seems to be no cIOS map at "{path}"')
        except ElementTree.ParseError as e:
            print(f'ParseError occurred trying to parse vWii cIOS map at "{path}":\n{e}')
        except Exception as e:
            print(f'{type(e).__name__} occurred trying to load/parse vWii cIOS map at "{path}":\n{e}')
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
        for widget in self.findChildren(QCheckBox, QRegularExpression('_d2x$')):
            widget.setIcon(resources.icons['blank_24'])
        for widget in self.findChildren(QCheckBox, QRegularExpression('_vWii$')):
            widget.setIcon(resources.icons['recommended_24'])

        if self.wiiMap is not None:
            self.setTitle(f'{self.wiiMap.find('ciosgroup').get('name')} cIOSs')
        else: return

        for base in [37, 38, 53, 55, 56, 57, 58, 60, 70, 80]:
            enabled = self.isIOSBaseAvailable(base, self.wiiMap)
            self.findChild(QLabel, f'b{base}').setEnabled(enabled)
            if enabled:
                self.findChild(QLabel, 'wiilabel').setEnabled(True)
            for widget in self.findChildren(QCheckBox, QRegularExpression(f'{base}_d2x$')):
                widget.setEnabled(enabled)
        if self.vWiiMap is not None:
            for base in [38, 56, 57, 58]:
                self.findChild(QLabel, 'vwiilabel').setEnabled(True)
                enabled = self.isIOSBaseAvailable(base, self.vWiiMap)
                self.findChild(QLabel, f'bv{base}').setEnabled(enabled)
                for widget in self.findChildren(QCheckBox, QRegularExpression(f'{base}_d2x_vWii$')):
                    widget.setEnabled(enabled)

        for item in config['recommendedWiiCios']:
            self.findChild(QCheckBox, f'c{item['slot']}_{item['base']}_d2x').setIcon(resources.icons['recommended_24'])

class WaninCheckGrid(CiosGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WaninCheckGrid()
        self.ui.setupUi(self)
        self.ui.select.clicked.connect(self.selectAll)
