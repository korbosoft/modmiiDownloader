# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QAbstractItemView, QApplication, QGroupBox, QListView

from PySide6.QtGui import QStandardItem, QStandardItemModel

from PySide6.QtCore import QMetaObject

from webbrowser import open_new

from resources import icons

class DownloadableItem(QStandardItem):

    def setAttrs(self, json):
        self.setToolTip(json['toolTip'])
        self.specialAttrs['id'] = json['id']
        self.specialAttrs['tags'] = json['tags']
        if 'url' in json:
            self.specialAttrs['url'] = json['url'];
        if 'disabled' in self.specialAttrs['tags']:
            self.setEnabled(False)
        if 'recommended' in self.specialAttrs['tags']:
            self.setIcon(icons['recommended_16'])
        elif 'semi-recommended' in self.specialAttrs['tags']:
            self.setIcon(icons['semiRecommended_16'])
        elif 'auto-updates' in self.specialAttrs['tags']:
            self.setIcon(icons['update_16'])
        else:
            self.setIcon(icons['blank_16'])
        if self.specialAttrs['url'] is not None:
            self.setForeground(QApplication.palette().link())
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
        if self.model().itemFromIndex(index).specialAttrs['url'] is not None:
            self.model().itemFromIndex(index).setForeground(QApplication.palette().linkVisited())
            open_new(self.model().itemFromIndex(index).specialAttrs['url'])

    def getSelected(self):
        return [self.model().itemFromIndex(index).specialAttrs['id'] for index in self.selectedIndexes()]

    def __init__(self, parent=None):
        super().__init__(parent)
        model = QStandardItemModel()
        self.setModel(model)
        self.clicked.connect(self.listClicked)

class DownloadListSection(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('DownloadListSection')
        self.list = DownloadList(self)
        self.list.setObjectName('list')
        self.list.move(3, 22)
        self.list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list.setProperty('showDropIndicator', False)
        self.list.setAlternatingRowColors(True)
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.list.setUniformItemSizes(True)

        QMetaObject.connectSlotsByName(self)
    def resizeEvent(self, event):
        self.list.resize(self.width() - 5, self.height() - 24)

