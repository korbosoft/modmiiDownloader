# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow

from ui_SearchDialog import Ui_SearchDialog

from downloadWidgets import DownloadableItem, DownloadListSection

import resources

class SearchDialog(QDialog):
    ui = Ui_SearchDialog()
    main = None

    def setupList(self, page: str, cat: str, list, query: str):
        for i in self.main.json['downloadList'][page][cat]['item']:
            index = list.model().rowCount()
            name = i['name']
            if query.lower() in name.lower():
                list.model().appendRow(DownloadableItem(name))
                list.model().item(index).setAttrs(i, page, cat)
            elif 'altname' in i:
                if query.lower() in i['altname'].lower():
                    list.model().appendRow(DownloadableItem(i['name']))
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
            self.main.findChild(DownloadListSection, item.specialAttrs['cat']).selectChild(item.specialAttrs['id'])
        self.close()

    def search(self, query):
        results = self.ui.results.list
        results.model().removeRows(0, results.model().rowCount())
        for section in self.main.sections:
            self.setupList(section[0], section[1], results, query)
        if results.model().rowCount() == 0:
            results.model().appendRow(DownloadableItem(f'No results for "{query}"'))
            results.model().item(0).setEnabled(False)

    def __init__(self, parent=None):
        super().__init__(parent)
        for widget in QApplication.instance().topLevelWidgets():
            if isinstance(widget, QMainWindow):
                self.main = widget

        self.ui.setupUi(self)
        self.ui.query.textChanged.connect(self.search)
        self.ui.add.setIcon(resources.icons['plus_16'])
        self.ui.add.clicked.connect(self.addSelected)
        self.ui.remove.setIcon(resources.icons['minus_16'])
        self.ui.remove.clicked.connect(self.removeSelected)
        self.ui.confirm.clicked.connect(self.confirm)
        self.ui.cancel.clicked.connect(self.close)

