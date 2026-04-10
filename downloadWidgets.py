# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import (QApplication, QGroupBox, QListView, QAbstractItemView,
QCheckBox, QVBoxLayout, QLabel, QSizePolicy, QMessageBox, QPushButton)

from PySide6.QtGui import QStandardItem, QStandardItemModel

from PySide6.QtCore import QMetaObject, Qt, QItemSelectionModel, Slot

from resources import icons

from webbrowser import open_new
import typing

class VertCheck(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(sizePolicy.hasHeightForWidth())
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        self.label = QLabel(self)
        self.label.setObjectName('label')
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.label)

        self.checkbox = QCheckBox(self)
        self.checkbox.setObjectName('checkbox')
        self.checkbox.setSizePolicy(sizePolicy)
        self.checkbox.setStyleSheet('QCheckBox {spacing: 0px} QCheckBox::indicator {subcontrol-position: top center}')

        self.layout.addWidget(self.checkbox)
    def setText(self, text):
        self.label.setText(text)

class DownloadableItem(QStandardItem):
    def setAttrs(self, json: dict, page: str, cat: str):
        self.setToolTip(json['toolTip'])
        self.specialAttrs['id'] = json['id']
        self.specialAttrs['tags'] = json['tags']
        self.specialAttrs['page'] = page
        self.specialAttrs['cat'] = cat
        if 'url' in json:
            self.specialAttrs['url'] = json['url']
        if 'warning' in json:
            self.specialAttrs['warning'] = json['warning']
        if 'disabled' in self.specialAttrs['tags']:
            self.setEnabled(False)
        if 'altname' in json:
            self.specialAttrs['altname'] = json['altname']
        if 'recommended' in self.specialAttrs['tags']:
            self.setIcon(icons['recommended_16'])
        elif 'semi-recommended' in self.specialAttrs['tags']:
            self.setIcon(icons['semiRecommended_16'])
        elif 'auto-updates' in self.specialAttrs['tags']:
            self.setIcon(icons['update_16'])
        elif 'semi-auto-updates' in self.specialAttrs['tags']:
            self.setIcon(icons['semiAutoUpdate_16'])
        else:
            self.setIcon(icons['blank_16'])
        if self.specialAttrs['url'] is not None:
            self.setForeground(QApplication.palette().link())
            font = self.font()
            font.setUnderline(True)
            self.setFont(font)

    def copyAttrs(self, item: typing.Self):
        self.setToolTip(item.toolTip())
        self.specialAttrs['id'] = item.specialAttrs['id']
        self.specialAttrs['altname'] = item.specialAttrs['altname']
        self.specialAttrs['tags'] = item.specialAttrs['tags']
        self.specialAttrs['url'] = item.specialAttrs['url']
        self.specialAttrs['warning'] = item.specialAttrs['warning']
        self.specialAttrs['page'] =item.specialAttrs['page']
        self.specialAttrs['cat'] = item.specialAttrs['cat']
        if not item.isEnabled():
            self.setEnabled(False)
        if 'recommended' in self.specialAttrs['tags']:
            self.setIcon(icons['recommended_16'])
        elif 'semi-recommended' in self.specialAttrs['tags']:
            self.setIcon(icons['semiRecommended_16'])
        elif 'auto-updates' in self.specialAttrs['tags']:
            self.setIcon(icons['update_16'])
        elif 'semi-auto-updates' in self.specialAttrs['tags']:
            self.setIcon(icons['semiAutoUpdate_16'])
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
            'altname': None,
            'url': None,
            'warning': None,
            'page': None,
            'cat': None
        }

class DownloadList(QListView):
    def listClicked(self, index):
        if self.model().itemFromIndex(index).specialAttrs['url'] is not None:
            self.model().itemFromIndex(index).setForeground(QApplication.palette().linkVisited())
            open_new(self.model().itemFromIndex(index).specialAttrs['url'])
        if self.model().itemFromIndex(index).specialAttrs['warning'] is not None:
            if index in self.selectionModel().selectedIndexes():
                ret = QMessageBox.warning(self, "Warning", self.model().itemFromIndex(index).specialAttrs['warning'], QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

                if ret != QMessageBox.StandardButton.Yes:
                    self.selectionModel().select(index, QItemSelectionModel.SelectionFlag.Deselect)

    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(parent)
        model = QStandardItemModel()
        self.setModel(model)
        self.clicked.connect(self.listClicked)

class DownloadListSection(QGroupBox):
    def __init__(self, parent=None, list=None):
        super().__init__(parent)
        self.setObjectName('DownloadListSection')

        if list is not None:
            self.list = list(self)
        else:
            self.list = DownloadList(self)

        self.list.setObjectName('list')
        self.list.move(5, 22)
        self.list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list.setProperty('showDropIndicator', False)
        self.list.setAlternatingRowColors(True)
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.list.setUniformItemSizes(True)

        self.select = QPushButton(self)
        self.select.setText('Select All')
        self.select.clicked.connect(self.toggleAllItems)

    @Slot()
    def toggleAllItems(self):
        selected = []
        for i in range(self.list.model().rowCount()):
            if self.list.model().item(i).isEnabled():
                selected.append(self.list.selectionModel().isSelected(self.list.model().item(i).index()))
            else:
                selected.append(True)
        for i in range(self.list.model().rowCount()):
            if self.list.model().item(i).isEnabled():
                self.list.selectionModel().select(self.list.model().item(i).index(), QItemSelectionModel.SelectionFlag.Select if False in selected else QItemSelectionModel.SelectionFlag.Deselect)

    def deselectAllItems(self):
        for i in range(self.list.model().rowCount()):
            if self.list.model().item(i).isEnabled():
                self.list.selectionModel().select(self.list.model().item(i).index(), QItemSelectionModel.SelectionFlag.Deselect)

    def selectChild(self, name):
        for i in range(self.list.model().rowCount()):
            if self.list.model().item(i).specialAttrs['id'] == name:
                self.list.selectionModel().select(self.list.model().item(i).index(), QItemSelectionModel.SelectionFlag.Select)

    def toggleChild(self, name):
        for i in range(self.list.model().rowCount()):
            if self.list.model().item(i).specialAttrs['id'] == name:
                self.list.selectionModel().select(self.list.model().item(i).index(), QItemSelectionModel.SelectionFlag.Toggle)

    def getSelected(self):
        str = ''
        for i in range(self.list.model().rowCount()):
            if 'disabled' not in self.list.model().item(i).specialAttrs['tags']:
                str = str + f'set {self.list.model().item(i).specialAttrs['id']}={'*' if self.list.selectionModel().isSelected(self.list.model().item(i).index()) else ''}\n'
        return str

    def getSelectedItems(self):
        list = []
        for i in range(self.list.model().rowCount()):
            if 'disabled' not in self.list.model().item(i).specialAttrs['tags']:
                if self.list.selectionModel().isSelected(self.list.model().item(i).index()):
                    list.append(self.list.model().item(i))
        return list

    def resizeEvent(self, event):
        self.list.resize(self.width() - 9, self.height() - 56)
        self.select.resize(self.width() - 9, 30)
        self.select.move(5, self.list.height() + 22)


