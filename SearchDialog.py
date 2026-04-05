# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow

from PySide6.QtCore import QEvent

from ui_SearchDialog import Ui_SearchDialog

from downloadWidgets import DownloadableItem, DownloadListSection

import resources

class SearchDialog(QDialog):
    ui = Ui_SearchDialog()
    main = None

    def setupList(self, page: str, cat: str, list, query: str):
        for i in self.main.json['downloadList'][page][cat]['item']:
            index = list.model().rowCount()
            if query.lower() in i['title'].lower():
                list.model().appendRow(DownloadableItem(i['title']))
                list.model().item(index).setAttrs(i, page, cat)

    def addSelected(self):
        items = self.ui.results.getSelectedItems()
        queueModel = self.ui.queue.list.model()
        for item in items:
            duplicate = False
            for i in range(self.ui.results.list.model().rowCount()):
                if queueModel.item(i) is not None:
                    if item.specialAttrs['id'] == queueModel.item(i).specialAttrs['id']:
                        duplicate = True
            if not duplicate:
                index = queueModel.rowCount()
                queueModel.appendRow(DownloadableItem(item.text()))
                queueModel.item(index).copyAttrs(item)
        self.ui.results.deselectAllItems()

    def removeSelected(self):
        items = self.ui.queue.getSelectedItems()
        for item in items:
            self.ui.queue.list.model().removeRow(item.row())

    def confirm(self):
        queueModel = self.ui.queue.list.model()
        for index in range(queueModel.rowCount()):
            item = queueModel.item(index)
            print(item.specialAttrs['cat'])
            print(item.specialAttrs['id'])
            self.main.findChild(DownloadListSection, item.specialAttrs['cat']).selectChild(item.specialAttrs['id'])
        self.close()

    def search(self):
        results = self.ui.results.list
        results.model().removeRows(0, results.model().rowCount())
        query = self.ui.query.text()
        self.setupList('nus', 'sysmenus', results, query)
        self.setupList('nus', 'realsigned', results, query)
        self.setupList('nus', 'fakesigned', results, query)
        self.setupList('nus', 'content', results, query)
        self.setupList('nus', 'channels', results, query)
        self.setupList('nus', 'other', results, query)
        self.setupList('wiiHaxx', 'exploits', results, query)
        self.setupList('wiiHaxx', 'wiiHomebrew', results, query)
        self.setupList('wiiHaxx', 'vWiiHomebrew', results, query)
        self.setupList('wiiHaxx', 'bothHomebrew', results, query)
        self.setupList('wiiHaxx', 'hbc', results, query)
        self.setupList('cios', 'hermes', results, query)
        self.setupList('cios', 'cmios', results, query)
        self.setupList('misc', 'pc', results, query)
        self.setupList('misc', 'wiiuHomebrew', results, query)
        if results.model().rowCount() == 0:
            results.model().appendRow(DownloadableItem(f'No results for "{query}"'))
            results.model().item(0).setEnabled(False)

    def __init__(self, parent=None):
        super().__init__(parent)
        for widget in QApplication.instance().topLevelWidgets():
            if isinstance(widget, QMainWindow):
                self.main = widget

        self.ui.setupUi(self)
        self.ui.search.setIcon(resources.icons['search_16'])
        self.ui.search.clicked.connect(self.search)
        self.ui.add.setIcon(resources.icons['plus_16'])
        self.ui.add.clicked.connect(self.addSelected)
        self.ui.remove.setIcon(resources.icons['minus_16'])
        self.ui.remove.clicked.connect(self.removeSelected)
        self.ui.confirm.clicked.connect(self.confirm)
        self.ui.cancel.clicked.connect(self.close)

