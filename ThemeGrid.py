# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QWidget, QCheckBox

from ui_ThemeGrid import Ui_ThemeGrid

from utils import toggleCheckBoxes

from webbrowser import open_new

class ThemeGrid(QWidget):
    def getSelected(self):
        str = ''
        for i in self.findChildren(QCheckBox):
            str = str + f'set {i.objectName()}={'*' if i.isEnabled() and i.isChecked() else ''}\n'
        return str

    def selectChild(self, name):
        child = self.findChild(QCheckBox, name)
        if child is not None:
            child.setChecked(True)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ThemeGrid()
        self.ui.setupUi(self)
        self.ui.s43U.clicked.connect(lambda: toggleCheckBoxes(self, '43U', True))
        self.ui.s42U.clicked.connect(lambda: toggleCheckBoxes(self, '42U', True))
        self.ui.s41U.clicked.connect(lambda: toggleCheckBoxes(self, '41U', True))
        self.ui.s43E.clicked.connect(lambda: toggleCheckBoxes(self, '43E', True))
        self.ui.s42E.clicked.connect(lambda: toggleCheckBoxes(self, '42E', True))
        self.ui.s41E.clicked.connect(lambda: toggleCheckBoxes(self, '41E', True))
        self.ui.s43J.clicked.connect(lambda: toggleCheckBoxes(self, '43J', True))
        self.ui.s42J.clicked.connect(lambda: toggleCheckBoxes(self, '42J', True))
        self.ui.s41J.clicked.connect(lambda: toggleCheckBoxes(self, '41J', True))
        self.ui.s43K.clicked.connect(lambda: toggleCheckBoxes(self, '43K', True))
        self.ui.s42K.clicked.connect(lambda: toggleCheckBoxes(self, '42K', True))
        self.ui.s41K.clicked.connect(lambda: toggleCheckBoxes(self, '41K', True))
        self.ui.svU.clicked.connect(lambda: toggleCheckBoxes(self, 'vU', True))
        self.ui.svE.clicked.connect(lambda: toggleCheckBoxes(self, 'vE', True))
        self.ui.svJ.clicked.connect(lambda: toggleCheckBoxes(self, 'vJ', True))
        self.ui.a.clicked.connect(lambda: toggleCheckBoxes(self, 'O_', True))
        self.ui.b.clicked.connect(lambda: toggleCheckBoxes(self, 'DarkWii_Red_...?$', True))
        self.ui.c.clicked.connect(lambda: toggleCheckBoxes(self, 'DarkWii_Green_...?$', True))
        self.ui.d.clicked.connect(lambda: toggleCheckBoxes(self, 'DarkWii_Blue_...?$', True))
        self.ui.e.clicked.connect(lambda: toggleCheckBoxes(self, 'DarkWii_Orange_...?$', True))
        self.ui.f.clicked.connect(lambda: toggleCheckBoxes(self, 'DarkWii_Red_\\d\\d._W', True))
        self.ui.g.clicked.connect(lambda: toggleCheckBoxes(self, 'DarkWii_Green_\\d\\d._W', True))
        self.ui.h.clicked.connect(lambda: toggleCheckBoxes(self, 'DarkWii_Blue_\\d\\d._W', True))
        self.ui.i.clicked.connect(lambda: toggleCheckBoxes(self, 'DarkWii_Orange_\\d\\d._W', True))
        self.ui.youtube.clicked.connect(lambda: open_new('https://modmii.github.io/WiiThemes.html'))
