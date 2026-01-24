# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QListView, QGroupBox

from PySide6.QtGui import QStandardItem, QStandardItemModel, QBrush

import webbrowser

class DownloadableItem(QStandardItem):
    def setAttrs(self, toolTip, id, tags, url=None):
        self.setToolTip(toolTip)
        self.specialAttrs['id'] = id
        self.specialAttrs['tags'] = tags
        self.specialAttrs['url'] = url;
        if 'disabled' in self.specialAttrs['tags']:
            self.setEnabled(False)
        if self.specialAttrs['url'] is not None:
            self.setForeground(QBrush(QApplication.palette().link()))
            font = self.font()
            font.setUnderline(True)
            self.setFont(font)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.specialAttrs = {
            'id': None,
            'tags': [],
            'url': None
        }

class DownloadList(QListView):
    def listClicked(self, index):
        print(self.getSelected())
        if self.model().itemFromIndex(index).specialAttrs['url'] is not None:
            self.model().itemFromIndex(index).setForeground(QBrush(QApplication.palette().linkVisited()))
            webbrowser.open_new(self.model().itemFromIndex(index).specialAttrs['url'])

    def getSelected(self):
        return [self.model().itemFromIndex(index).specialAttrs['id'] for index in self.selectedIndexes()]

    def __init__(self, parent=None):
        super().__init__(parent)
        model = QStandardItemModel()
        self.setModel(model)
        self.clicked.connect(self.listClicked)

from ui_DownloadListSection import Ui_DownloadListSection

class DownloadListSection(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DownloadListSection()
        self.ui.setupUi(self)

    def resizeEvent(self, event):
        print(self.width())
        self.ui.list.resize(self.width() - 5, self.height() - 24)

