# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow

from PySide6.QtCore import QEvent

from ui_SearchDialog import Ui_SearchDialog

from downloadWidgets import DownloadableItem, DownloadListSection

class SearchDialog(QDialog):
    ui = Ui_SearchDialog()
    main = None

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

    def removeSelected(self):
        items = self.ui.queue.getSelectedItems()
        for item in items:
            self.ui.queue.list.model().removeRow(item.row())

    def okPressed(self):
        pass

    def search(self):
        self.ui.results.list.model().removeRows(0, self.ui.results.list.model().rowCount())
        self.main.setupList('wiiHaxx', 'exploits', self.ui.results.list)
        pass

    def __init__(self, parent=None):
        super().__init__(parent)
        for widget in QApplication.instance().topLevelWidgets():
            if isinstance(widget, QMainWindow):
                self.main = widget

        self.ui.setupUi(self)
        self.ui.search.clicked.connect(self.search)
        self.ui.add.clicked.connect(self.addSelected)
        self.ui.remove.clicked.connect(self.removeSelected)
        self.ui.ok.clicked.connect(self.okPressed)
        self.ui.cancel.clicked.connect(self.close)

