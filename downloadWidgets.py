# This Python file uses the following encoding: utf-8

import typing
from webbrowser import open_new

from PySide6.QtWidgets import (QApplication, QGroupBox, QListView, QAbstractItemView,
                             QCheckBox, QVBoxLayout, QLabel, QSizePolicy, QMessageBox, QPushButton)
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import Qt, QItemSelectionModel, Slot

from resources import icons

ID_ROLE = Qt.ItemDataRole.UserRole + 1


class VertCheck(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(sizePolicy.hasHeightForWidth())

        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        self.layout.setContentsMargins(0, 0, 0, 0)

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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.specialAttrs = {
            'tags': [],
            'altname': None,
            'url': None,
            'warning': None,
            'page': None,
            'cat': None
        }

    def setAttrs(self, json: dict, page: str, cat: str):
        self.setData(json['id'], ID_ROLE)
        self.setToolTip(json['toolTip'])
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
        self.setData(item.data(ID_ROLE), ID_ROLE)
        self.setToolTip(item.toolTip())
        self.specialAttrs['altname'] = item.specialAttrs['altname']
        self.specialAttrs['tags'] = item.specialAttrs['tags']
        self.specialAttrs['url'] = item.specialAttrs['url']
        self.specialAttrs['warning'] = item.specialAttrs['warning']
        self.specialAttrs['page'] = item.specialAttrs['page']
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


class DownloadList(QListView):
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(parent)
        model = QStandardItemModel()
        self.setModel(model)
        self.clicked.connect(self.listClicked)

    def listClicked(self, index):
        item = self.model().itemFromIndex(index)
        if item.specialAttrs['url'] is not None:
            item.setForeground(QApplication.palette().linkVisited())
            open_new(item.specialAttrs['url'])

        if item.specialAttrs['warning'] is not None:
            if index in self.selectionModel().selectedIndexes():
                ret = QMessageBox.warning(
                    self,
                    "Warning",
                    item.specialAttrs['warning'],
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel
                )
                if ret != QMessageBox.StandardButton.Yes:
                    self.selectionModel().select(index, QItemSelectionModel.SelectionFlag.Deselect)


class DownloadListSection(QGroupBox):
    def __init__(self, parent=None, item_list=None):
        super().__init__(parent)
        self.setObjectName('DownloadListSection')

        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 10, 5, 5)
        layout.setSpacing(5)

        if item_list is not None:
            self.item_list = item_list(self)
        else:
            self.item_list = DownloadList(self)

        self.item_list.setObjectName('list')
        self.item_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.item_list.setProperty('showDropIndicator', False)
        self.item_list.setAlternatingRowColors(True)
        self.item_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.item_list.setUniformItemSizes(True)

        layout.addWidget(self.item_list)

        self.select = QPushButton(self)
        self.select.setText('Toggle All')
        self.select.setFixedHeight(30)
        self.select.clicked.connect(self.toggleAllItems)

        layout.addWidget(self.select)

    @Slot()
    def toggleAllItems(self):
        model = self.item_list.model()
        selected = []
        for i in range(model.rowCount()):
            if model.item(i).isEnabled():
                selected.append(self.item_list.selectionModel().isSelected(model.item(i).index()))
            else:
                selected.append(True)
        for i in range(model.rowCount()):
            if model.item(i).isEnabled():
                self.item_list.selectionModel().select(
                    model.item(i).index(),
                    QItemSelectionModel.SelectionFlag.Select if False in selected else QItemSelectionModel.SelectionFlag.Deselect
                )

    def deselectAllItems(self):
        model = self.item_list.model()
        for i in range(model.rowCount()):
            if model.item(i).isEnabled():
                self.item_list.selectionModel().select(model.item(i).index(), QItemSelectionModel.SelectionFlag.Deselect)

    def selectChild(self, item_id):
        model = self.item_list.model()
        matches = model.match(model.index(0, 0), ID_ROLE, item_id, hits=1, flags=Qt.MatchFlag.MatchExactly)
        for index in matches:
            if model.item(index.row()).isEnabled():
                self.item_list.selectionModel().select(index, QItemSelectionModel.SelectionFlag.Select)

    def toggleChild(self, item_id):
        model = self.item_list.model()
        matches = model.match(model.index(0, 0), ID_ROLE, item_id, hits=1, flags=Qt.MatchFlag.MatchExactly)
        for index in matches:
            self.item_list.selectionModel().select(index, QItemSelectionModel.SelectionFlag.Toggle)

    def getSelected(self):
        model = self.item_list.model()
        out_str = ''
        for i in range(model.rowCount()):
            if 'disabled' not in model.item(i).specialAttrs['tags']:
                index = model.item(i).index()
                is_selected = '*' if self.item_list.selectionModel().isSelected(index) else ''
                out_str += f'set {model.data(index, ID_ROLE)}={is_selected}\n'
        return out_str

    def getSelectedItems(self):
        model = self.item_list.model()
        selected = []
        for i in range(model.rowCount()):
            if 'disabled' not in model.item(i).specialAttrs['tags']:
                if self.item_list.selectionModel().isSelected(model.item(i).index()):
                    selected.append(model.item(i))
        return selected