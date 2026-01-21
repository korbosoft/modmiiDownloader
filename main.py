# This Python file uses the following encoding: utf-8
import sys, json

from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtCore import Qt

from PySide6.QtGui import QStandardItem, QStandardItemModel

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_mainWindow import Ui_mainWindow

# Define a custom role for your attribute
ID_ROLE = Qt.UserRole + 1

def select_by_attribute(view, target_id):
    model = view.model()
    # Search the model using your custom role
    matches = model.match(
        model.index(0, 0),
        ID_ROLE,
        target_id,
        1,
        Qt.MatchExactly
    )

    if matches:
        view.setCurrentIndex(matches[0])

class mainWindow(QMainWindow):
    class Downloadable(QStandardItem):
        specialAttrs = {
            'id': None,
            'flags': []
        }

        def setAttrs(self, toolTip, id, flags):
            self.setToolTip(toolTip)
            self.specialAttrs['id'] = id
            self.specialAttrs['flags'] = flags

        def __init__(self, parent=None):
            super().__init__(parent)

    ui = Ui_mainWindow()
    downloadList = None;

    def setup(self):
        sysmenuModel = QStandardItemModel()
        self.ui.sysmenuList.setModel(sysmenuModel)
        for i in self.downloadList['sysMenus']['item']:
            self.ui.sysmenuList.model().appendRow(self.Downloadable(i['title']))

        realsignedModel = QStandardItemModel()
        self.ui.realsignedList.setModel(realsignedModel)
        for i in self.downloadList['realsigned']['item']:
            row = self.ui.realsignedList.model().rowCount()
            self.ui.realsignedList.model().appendRow(self.Downloadable(i['title']))
            self.ui.realsignedList.model().item(row).setAttrs(i['toolTip'], i['id'], i['flags'])

        fakesignedModel = QStandardItemModel()
        self.ui.fakesignedList.setModel(fakesignedModel)
        for i in self.downloadList['fakesigned']['item']:
            row = self.ui.fakesignedList.model().rowCount()
            self.ui.fakesignedList.model().appendRow(self.Downloadable(i['title']))
            self.ui.fakesignedList.model().item(row).setAttrs(i['toolTip'], i['id'], i['flags'])

        contentModel = QStandardItemModel()
        self.ui.contentList.setModel(contentModel)
        for i in self.downloadList['content']['item']:
            row = self.ui.contentList.model().rowCount()
            self.ui.contentList.model().appendRow(self.Downloadable(i['title']))
            self.ui.contentList.model().item(row).setAttrs(i['toolTip'], i['id'], i['flags'])

        channelModel = QStandardItemModel()
        self.ui.channelList.setModel(channelModel)
        for i in self.downloadList['channels']['item']:
            row = self.ui.channelList.model().rowCount()
            self.ui.channelList.model().appendRow(self.Downloadable(i['title']))
            self.ui.channelList.model().item(row).setAttrs(i['toolTip'], i['id'], i['flags'])

        contentModel = QStandardItemModel()
        self.ui.otherList.setModel(contentModel)
        for i in self.downloadList['other']['item']:
            row = self.ui.otherList.model().rowCount()
            self.ui.otherList.model().appendRow(self.Downloadable(i['title']))
            self.ui.otherList.model().item(row).setAttrs(i['toolTip'], i['id'], i['flags'])


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui.setupUi(self)
        with open('download.json') as j:
            try:
                self.downloadList = json.load(j)
            except:
                raise Exception('DOWNLOAD LIST FAILED, ABORT!!')
        self.setup()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = mainWindow()
    widget.show()
    sys.exit(app.exec())
