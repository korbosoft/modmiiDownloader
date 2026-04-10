# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QHBoxLayout, QLineEdit, QPushButton, QWidget
from PySide6.QtGui import QStandardItemModel
from PySide6.QtCore import QRect

from downloadWidgets import DownloadableItem, DownloadListSection, DownloadList

import re

import resources

class SearchList(DownloadList):
    parent = None

    def add(self, index):
        QApplication.activeWindow().addItem(index)

    def remove(self, index):
        self.model().removeRow(index.row())

    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(parent)
        model = QStandardItemModel()
        self.setModel(model)

class QueueList(SearchList):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.doubleClicked.connect(self.remove)

class ResultsList(SearchList):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.doubleClicked.connect(self.add)

class SearchListSection(DownloadListSection):
    parent = None

    def __init__(self, parent=None, queue=False):
        self.parent = parent

        if queue:
            super().__init__(parent, QueueList)
        else:
            super().__init__(parent, ResultsList)

        self.setObjectName('SearchListSection')

class SearchDialog(QDialog):
    main = None
    sanitizer = re.compile(r'[^a-z0-9\s]')

    def searchList(self, page: str, cat: str, list, query: str):
        query = self.sanitizer.sub('', query.lower())
        for i in self.main.json['downloadList'][page][cat]['item']:
            name = self.sanitizer.sub('', i['name'].lower())
            index = list.model().rowCount()
            if query.lower() in name.lower():
                list.model().appendRow(DownloadableItem(i['name']))
                list.model().item(index).setAttrs(i, page, cat)
            elif 'altnames' in i:
                for altname in i['altnames']:
                    if query.lower() in self.sanitizer.sub('', altname.lower()):
                        list.model().appendRow(DownloadableItem(i['name']))
                        list.model().item(index).setAttrs(i, page, cat)

    def addSelected(self):
        items = self.results.getSelectedItems()
        queueModel = self.queue.list.model()
        for item in items:
            duplicate = False
            for i in range(self.results.list.model().rowCount()):
                if queueModel.item(i) is not None:
                    if item.specialAttrs['id'] == queueModel.item(i).specialAttrs['id']:
                        duplicate = True
            if not duplicate:
                index = queueModel.rowCount()
                queueModel.appendRow(DownloadableItem(item.text()))
                queueModel.item(index).copyAttrs(item)
        self.results.deselectAllItems()

    def removeSelected(self):
        items = self.queue.getSelectedItems()
        for item in items:
            self.queue.list.model().removeRow(item.row())

    def addItem(self, index):
        queueModel = self.queue.list.model()
        duplicate = False
        item = self.results.list.model().item(index.row())
        for i in range(self.results.list.model().rowCount()):
            if queueModel.item(i) is not None:
                if item.specialAttrs['id'] == queueModel.item(i).specialAttrs['id']:
                    duplicate = True
        if not duplicate:
            index = queueModel.rowCount()
            queueModel.appendRow(DownloadableItem(item.text()))
            queueModel.item(index).copyAttrs(item)

    def confirm(self):
        queueModel = self.queue.list.model()
        if queueModel.rowCount():
            msgBox = QMessageBox(self)
            msgBox.setText('Do you want to save your changes?')
            msgBox.setInformativeText(f'This will add {queueModel.rowCount()} items to the queue.')
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.StandardButton.Cancel)
            msgBox.setDefaultButton(QMessageBox.Cancel)
            msgBox.setDetailedText('Selected items:\n' + '\n'.join([queueModel.item(index).text() for index in range(queueModel.rowCount())]))
            match msgBox.exec():
                case QMessageBox.StandardButton.Cancel:
                    pass
                case QMessageBox.Save:
                    for index in range(queueModel.rowCount()):
                        item = queueModel.item(index)
                        self.main.findChild(DownloadListSection, item.specialAttrs['cat']).selectChild(item.specialAttrs['id'])
                        self.close()
                case QMessageBox.Discard:
                    self.close()
        else: self.close()

    def search(self, query):
        query = self.sanitizer.sub('', query.lower())
        results = self.results.list
        results.model().removeRows(0, results.model().rowCount())
        if query != '':
            for section in self.main.sections:
                self.searchList(section[0], section[1], results, query)
            if results.model().rowCount() == 0:
                results.model().appendRow(DownloadableItem(f'No results for "{query}"'))
                results.model().item(0).setEnabled(False)

    def __init__(self, parent=None):
        super().__init__(parent)

        for widget in QApplication.instance().topLevelWidgets():
            if isinstance(widget, QMainWindow):
                self.main = widget

        if not self.objectName():
            self.setObjectName("SearchDialog")
        self.resize(400, 400)
        self.setWindowTitle("Search")
        self.setFixedSize(self.size())
        self.setWindowIcon(resources.icons['mainIcon'])
        self.add = QPushButton(self)
        self.add.setObjectName("add")
        self.add.setText("Add Selected")
        self.add.setGeometry(QRect(0, 30, 200, 30))
        self.add.setIcon(resources.icons['plus_16'])
        self.add.clicked.connect(self.addSelected)
        self.remove = QPushButton(self)
        self.remove.setObjectName("remove")
        self.remove.setText("Remove Selected")
        self.remove.setGeometry(QRect(200, 30, 200, 30))
        self.remove.setIcon(resources.icons['minus_16'])
        self.remove.clicked.connect(self.removeSelected)
        self.query = QLineEdit(self)
        self.query.setObjectName("query")
        self.query.setPlaceholderText("Enter query here...")
        self.query.setGeometry(QRect(0, 0, 400, 30))
        self.query.setClearButtonEnabled(True)
        self.query.textChanged.connect(self.search)
        self.doneButton = QPushButton(self)
        self.doneButton.setObjectName("done")
        self.doneButton.setText("Done")
        self.doneButton.setGeometry(QRect(0, 370, 400, 30))
        self.doneButton.clicked.connect(self.confirm)
        self.doneButton.setDefault(True)
        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 60, 400, 310))
        self.layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.layout.setObjectName("layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.results = SearchListSection(self.horizontalLayoutWidget)
        self.results.setObjectName("results")
        self.results.setTitle("Results")

        self.layout.addWidget(self.results)

        self.queue = SearchListSection(self.horizontalLayoutWidget, True)
        self.queue.setObjectName("queue")
        self.queue.setTitle("Queue")

        self.layout.addWidget(self.queue)

        QWidget.setTabOrder(self.query, self.add)
        QWidget.setTabOrder(self.add, self.remove)
        QWidget.setTabOrder(self.remove, self.doneButton)
