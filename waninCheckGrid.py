# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QGroupBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_waninCheckGrid import Ui_waninCheckGrid

class waninCheckGrid(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_waninCheckGrid()
        self.ui.setupUi(self)
