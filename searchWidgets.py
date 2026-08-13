# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QHBoxLayout, QLineEdit, QPushButton, QWidget
from PySide6.QtGui import QStandardItemModel
from PySide6.QtCore import QRect, QItemSelectionModel

from downloadWidgets import DownloadableItem, DownloadListSection, DownloadList, ID_ROLE

import re

import resources

from config import config

sanitizer = re.compile(r'[^a-z0-9\s]')

class SearchList(DownloadList):
    parent = None

    def add(self, index):
        QApplication.activeWindow().addItem(index)
        self.selectionModel().select(index, QItemSelectionModel.SelectionFlag.Deselect)

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

    def searchCheckboxes(self, query: str):
        query = sanitizer.sub('', query.lower())

        pass

    def searchList(self, page: str, cat: str, item_list, query: str, queued_ids):
        query = sanitizer.sub('', query.lower())
        for i in config['downloadList'][page][cat]['item']:

            if i.get('id') in queued_ids:
                continue

            name = sanitizer.sub('', i['name'].lower())
            index = item_list.model().rowCount()

            if query.lower() in name.lower():
                item_list.model().appendRow(DownloadableItem(i['name']))
                item_list.model().item(index).setAttrs(i, page, cat)

            elif 'altnames' in i:
                for altname in i['altnames']:
                    if query.lower() in sanitizer.sub('', altname.lower()):
                        item_list.model().appendRow(DownloadableItem(i['name']))
                        item_list.model().item(index).setAttrs(i, page, cat)
                        break

    def addSelected(self):
        items = self.results.getSelectedItems()
        queueModel = self.queue.item_list.model()

        for item in items:
            target_id = item.data(ID_ROLE)
            duplicate = False

            for i in range(queueModel.rowCount()):
                idx = queueModel.index(i, 0)
                queue_id = queueModel.data(idx, ID_ROLE)

                if queue_id == target_id:
                    duplicate = True
                    break

            if not duplicate:
                new_item = DownloadableItem(item.text())
                new_item.copyAttrs(item)
                queueModel.appendRow(new_item)

        self.results.deselectAllItems()

    def removeSelected(self):
        items = self.queue.getSelectedItems()
        for item in items:
            self.queue.item_list.model().removeRow(item.row())

    def addItem(self, index):
        queueModel = self.queue.item_list.model()
        resultsModel = self.results.item_list.model()

        item = resultsModel.item(index.row())
        if not item:
            return

        target_id = item.data(ID_ROLE)
        duplicate = False

        for i in range(queueModel.rowCount()):
            idx = queueModel.index(i, 0)
            queue_id = queueModel.data(idx, ID_ROLE)

            if queue_id == target_id:
                duplicate = True
                break

        if not duplicate:
            new_item = DownloadableItem(item.text())
            new_item.copyAttrs(item)
            queueModel.appendRow(new_item)

    def confirm(self):
        queueModel = self.queue.item_list.model()
        if queueModel.rowCount() or self.oldQueue.model().rowCount():
            msgBox = QMessageBox(self)
            msgBox.setText('Do you want to save your changes?')

            oldIDs = set()
            oldModel = self.oldQueue.model()
            for i in range(oldModel.rowCount()):
                item = oldModel.item(i)
                if item and hasattr(item, 'specialAttrs'):
                    item_id = oldModel.data(item.index(), ID_ROLE)
                    if item_id:
                        oldIDs.add(item_id)

            currentIDs = set()
            for i in range(queueModel.rowCount()):
                item = queueModel.item(i)
                if item and hasattr(item, 'specialAttrs'):
                    item_id = queueModel.data(item.index(), ID_ROLE)
                    if item_id:
                        currentIDs.add(item_id)

            addedCount = len(currentIDs - oldIDs)
            removedCount = len(oldIDs - currentIDs)

            info_lines = []
            if addedCount > 0:
                info_lines.append(f'{addedCount} new item{"s" if addedCount > 1 else ""}')
            if removedCount > 0:
                info_lines.append(f'{removedCount} removed item{"s" if removedCount > 1 else ""}')

            if info_lines:
                msgBox.setInformativeText("\n".join(info_lines))

            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.StandardButton.Cancel)
            msgBox.setDefaultButton(QMessageBox.Cancel)
            msgBox.setDetailedText('Selected items:\n' + '\n'.join([queueModel.item(index).text() for index in range(queueModel.rowCount())]))

            match msgBox.exec():
                case QMessageBox.StandardButton.Cancel:
                    pass
                case QMessageBox.Save:
                    for section in self.main.findChildren(DownloadListSection):
                        section.deselectAllItems()

                    for index in range(queueModel.rowCount()):
                        item = queueModel.item(index)
                        self.main.findChild(DownloadListSection, item.specialAttrs['cat']).selectChild(queueModel.data(item.index(), ID_ROLE))

                    self.close()
                case QMessageBox.Discard:
                    self.close()
        else: self.close()

    def search(self, query):
            query = sanitizer.sub('', query.lower())
            results = self.results.item_list
            resultsModel = results.model()
            queue = self.queue.item_list
            queueModel = queue.model()
            resultsModel.removeRows(0, resultsModel.rowCount())

            if query != '':
                queued_ids = {
                    queueModel.data(queueModel.item(i).index(), ID_ROLE)
                    for i in range(queueModel.rowCount())
                }

                queued_ids.discard(None)

                for section in self.main.sections:
                    self.searchList(section[0], section[1], results, query, queued_ids)

                if resultsModel.rowCount() == 0:
                    resultsModel.appendRow(DownloadableItem(f'No results for "{query}"'))
                    resultsModel.item(0).setEnabled(False)

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

        self.oldQueue = QueueList(self)
        self.oldQueue.setObjectName("oldQueue")
        self.oldQueue.hide()

        self.layout.addWidget(self.queue)

        for section in self.main.sections:
            for item in self.main.findChild(DownloadListSection, section[1]).getSelectedItems():
                queueModel = self.queue.item_list.model()
                oldQueueModel = self.oldQueue.model()

                q_item = DownloadableItem(item.text())
                q_item.copyAttrs(item)
                queueModel.appendRow(q_item)

                old_item = DownloadableItem(item.text())
                old_item.copyAttrs(item)
                oldQueueModel.appendRow(old_item)

        QWidget.setTabOrder(self.query, self.add)
        QWidget.setTabOrder(self.add, self.remove)
        QWidget.setTabOrder(self.remove, self.doneButton)
