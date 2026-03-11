# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QCheckBox, QGroupBox, QLabel, QWidget

from PySide6.QtCore import QRegularExpression

from xml.etree import ElementTree

from utils import toggleCheckBoxes

import resources

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
    paths = None
    recommendedWiiCios = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_D2xCheckGrid()
        self.ui.setupUi(self)
        self.ui.select.clicked.connect(self.selectAll)

    def setup(self, paths=None, recommendedWiiCios=None):
        if paths is not None and self.paths is None:
            self.paths = paths
        if recommendedWiiCios is not None and self.recommendedWiiCios is None:
            self.recommendedWiiCios = recommendedWiiCios
        self.loadD2xMaps()
        self.setupD2x()

    def toggleWiiRecommended(self):
        toggleCheckBoxes(self, [self.findChild(QCheckBox, f'c{cios['slot']}_{cios['base']}_d2x') for cios in self.recommendedWiiCios])

    def toggleVWiiRecommended(self):
        toggleCheckBoxes(self, '_vWii$', True)

    def loadD2xMaps(self):
        # load Wii cIOS map
        for i in self.paths['wiiMap']:
            try:
                print(f'Attempting to load "{i}"')
                self.wiiMap = ElementTree.parse(i).getroot()
                break
            except FileNotFoundError:
                print(f'There seems to be no cIOS map at "{i}"')
            except ElementTree.ParseError as e:
                print(f'ParseError occurred trying to parse Wii cIOS map at "{i}":\n{e}')
            except Exception as e:
                print(f'{type(e).__name__} occurred trying to load/parse Wii cIOS map at "{i}":\n{e}')
        if self.wiiMap is None:
            print('Failed to load/parse ciosmaps.xml, so no Wii d2x. This shouldn\'t ever happen?')
        else:
            print('Successfully loaded & parsed ciosmaps.xml!')
        # load vWii cIOS map
        for i in self.paths['vWiiMap']:
            try:
                print(f'Attempting to load "{i}"')
                self.vWiiMap = ElementTree.parse(i).getroot()
                break
            except FileNotFoundError:
                print(f'There seems to be no cIOS map at "{i}"')
            except ElementTree.ParseError as e:
                print(f'ParseError occurred trying to parse vWii cIOS map at "{i}":\n{e}')
            except Exception as e:
                print(f'{type(e).__name__} occurred trying to load/parse vWii cIOS map at "{i}":\n{e}')
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
        if self.wiiMap is None or self.vWiiMap is None:
            self.loadD2xMaps()

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
            for widget in self.findChildren(QCheckBox, QRegularExpression(f'{base}_d2x$')):
                widget.setEnabled(enabled)
        if self.vWiiMap is not None:
            for base in [38, 56, 57, 58]:
                self.findChild(QLabel, 'dv').setEnabled(True)
                enabled = self.isIOSBaseAvailable(base, self.vWiiMap)
                for widget in self.findChildren(QCheckBox, QRegularExpression(f'{base}_d2x_vWii$')):
                    widget.setEnabled(enabled)

        for item in self.recommendedWiiCios:
            self.findChild(QCheckBox, f'c{item['slot']}_{item['base']}_d2x').setIcon(resources.icons['recommended_24'])

class WaninCheckGrid(CiosGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WaninCheckGrid()
        self.ui.setupUi(self)
        self.ui.select.clicked.connect(self.selectAll)
