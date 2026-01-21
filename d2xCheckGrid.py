# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QGroupBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_d2xCheckGrid import Ui_d2xCheckGrid

class d2xCheckGrid(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_d2xCheckGrid()
        self.ui.setupUi(self)
