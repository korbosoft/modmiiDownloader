# This Python file uses the following encoding: utf-8

import re

from PySide6.QtCore import QItemSelectionModel
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import (
    QApplication, QCheckBox, QDialog, QHBoxLayout, QLineEdit,
    QMainWindow, QMessageBox, QPushButton, QVBoxLayout
)

from config import config
from downloadWidgets import DownloadableItem, DownloadList, DownloadListSection, ID_ROLE
import resources

sanitizer = re.compile(r'[^a-z0-9\s]')

class SearchList(DownloadList):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setModel(QStandardItemModel())

    def add(self, index):
        active_win = QApplication.activeWindow()
        if active_win and hasattr(active_win, "addItem"):
            active_win.addItem(index)
        self.selectionModel().select(index, QItemSelectionModel.SelectionFlag.Deselect)

    def remove(self, index):
        self.model().removeRow(index.row())

class QueueList(SearchList):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.doubleClicked.connect(self.remove)

class ResultsList(SearchList):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.doubleClicked.connect(self.add)

class SearchListSection(DownloadListSection):
    def __init__(self, parent=None, is_queue=False):
        list_cls = QueueList if is_queue else ResultsList
        super().__init__(parent, list_cls)
        self.setObjectName('SearchListSection')

class SearchDialog(QDialog):
    reverse_checkboxes = {val: key for key, val in config['checkboxNames'].items()}

    def closeEvent(self, event):
        if self.confirm():
            event.accept()
        else:
            event.ignore()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.main = next(
            (w for w in QApplication.topLevelWidgets() if isinstance(w, QMainWindow)),
            None
        )

        self.setObjectName("SearchDialog")
        self.setWindowTitle("Search")
        self.resize(450, 450)
        self.setWindowIcon(resources.icons['mainIcon'])

        self._init_ui()
        self._populate_initial_queue()

    def _init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 10, 5, 5)
        main_layout.setSpacing(5)

        self.query = QLineEdit(self)
        self.query.setPlaceholderText("Enter query here...")
        self.query.setClearButtonEnabled(True)
        self.query.textChanged.connect(self.search)
        main_layout.addWidget(self.query)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(5)
        self.add_btn = QPushButton("Add Selected", self, objectName="add")
        self.add_btn.setIcon(resources.icons['plus_16'])
        self.add_btn.clicked.connect(self.addSelected)

        self.remove_btn = QPushButton("Remove Selected", self, objectName="remove")
        self.remove_btn.setIcon(resources.icons['minus_16'])
        self.remove_btn.clicked.connect(self.removeSelected)

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.remove_btn)
        main_layout.addLayout(btn_layout)

        panes_layout = QHBoxLayout()
        panes_layout.setSpacing(5)

        self.results = SearchListSection(self)
        self.results.setObjectName("results")
        self.results.setTitle("Results")

        self.queue = SearchListSection(self, is_queue=True)
        self.queue.setObjectName("queue")
        self.queue.setTitle("Queue")

        panes_layout.addWidget(self.results)
        panes_layout.addWidget(self.queue)
        main_layout.addLayout(panes_layout)

        self.oldQueue = QueueList(self)
        self.oldQueue.setObjectName("oldQueue")
        self.oldQueue.hide()

        self.doneButton = QPushButton("Done", self, objectName="done")
        self.doneButton.setDefault(True)
        self.doneButton.clicked.connect(self.close)
        main_layout.addWidget(self.doneButton)

        self.setTabOrder(self.query, self.add_btn)
        self.setTabOrder(self.add_btn, self.remove_btn)
        self.setTabOrder(self.remove_btn, self.doneButton)

    def _get_checkbox_icon(self, real_name: str):
        match = re.match(r'^c(\d+)_(\d+)_', real_name)
        if match:
            slot, base = int(match.group(1)), int(match.group(2))

            for rec in config.get('recommendedWiiCios', []):
                if rec.get('slot') == slot and rec.get('base') == base:
                    return resources.icons.get('recommended_24')

        return resources.icons.get('blank_24')

    def _get_queue_ids(self) -> set:
        model = self.queue.item_list.model()
        return {
            model.data(model.index(i, 0), ID_ROLE)
            for i in range(model.rowCount())
        } - {None}

    def _sort_model(self, model):
        items = [model.takeRow(0)[0] for _ in range(model.rowCount())]
        items.sort(key=lambda item: item.text().lower())
        for item in items:
            model.appendRow(item)

    def _add_item_to_queue(self, source_item, queue_model, existing_ids: set) -> bool:
        target_id = source_item.data(ID_ROLE)
        if target_id in existing_ids:
            return False

        new_item = DownloadableItem(source_item.text())
        new_item.copyAttrs(source_item)

        icon = source_item.icon() if not source_item.icon().isNull() else resources.icons.get('blank_24')
        if icon:
            new_item.setIcon(icon)

        if hasattr(source_item, 'is_checkbox'):
            new_item.is_checkbox = source_item.is_checkbox
            new_item.real_name = getattr(source_item, 'real_name', None)

        queue_model.appendRow(new_item)
        existing_ids.add(target_id)

        self._sort_model(queue_model)
        return True

    def _populate_initial_queue(self):
        if not self.main:
            return

        queue_model = self.queue.item_list.model()
        old_model = self.oldQueue.model()

        if hasattr(self.main, 'sections'):
            for section in self.main.sections:
                sec_widget = self.main.findChild(DownloadListSection, section[1])
                if not sec_widget:
                    continue

                for item in sec_widget.getSelectedItems():
                    icon = item.icon() if not item.icon().isNull() else resources.icons.get('blank_24')

                    q_item = DownloadableItem(item.text())
                    q_item.copyAttrs(item)
                    if icon:
                        q_item.setIcon(icon)
                    queue_model.appendRow(q_item)

                    old_item = DownloadableItem(item.text())
                    old_item.copyAttrs(item)
                    if icon:
                        old_item.setIcon(icon)
                    old_model.appendRow(old_item)

        for check_box in self.main.findChildren(QCheckBox):
            if check_box.isEnabled() and check_box.isChecked():
                real_name = check_box.objectName()
                display_name = config['checkboxNames'].get(real_name)
                if not display_name:
                    continue

                if 'PLACEHOLDER' in display_name and hasattr(self.main, 'd2xRev'):
                    display_name = display_name.replace('PLACEHOLDER', f'd2x-v{self.main.d2xRev}')

                icon = self._get_checkbox_icon(real_name)

                cb_item = DownloadableItem(display_name)
                cb_item.setData(real_name, ID_ROLE)
                cb_item.is_checkbox = True
                cb_item.real_name = real_name
                if icon:
                    cb_item.setIcon(icon)

                old_item = DownloadableItem(display_name)
                old_item.setData(real_name, ID_ROLE)
                old_item.is_checkbox = True
                old_item.real_name = real_name
                if icon:
                    old_item.setIcon(icon)

                queue_model.appendRow(cb_item)
                old_model.appendRow(old_item)

        self._sort_model(queue_model)
        self._sort_model(old_model)

    def _search_checkboxes(self, query: str, queued_ids: set):
        if not self.main:
            return

        clean_query = sanitizer.sub('', query.lower())
        results_model = self.results.item_list.model()

        for check_box in self.main.findChildren(QCheckBox):
            if not check_box.isEnabled() or check_box.isChecked():
                continue

            real_name = check_box.objectName()
            if not real_name or real_name in queued_ids:
                continue

            display_name = config['checkboxNames'].get(real_name)
            if not display_name:
                continue

            clean_real_name = sanitizer.sub('', real_name.lower())
            clean_display_name = sanitizer.sub('', display_name.lower())

            if clean_query in clean_display_name or clean_query in clean_real_name:
                formatted_name = display_name
                if 'PLACEHOLDER' in formatted_name and hasattr(self.main, 'd2xRev'):
                    formatted_name = formatted_name.replace('PLACEHOLDER', f'd2x-v{self.main.d2xRev}')

                item = DownloadableItem(formatted_name)
                item.setData(real_name, ID_ROLE)
                item.is_checkbox = True
                item.real_name = real_name

                icon = self._get_checkbox_icon(real_name)
                if icon:
                    item.setIcon(icon)

                results_model.appendRow(item)

    def searchList(self, page: str, cat: str, item_list, query: str, queued_ids: set):
        clean_query = sanitizer.sub('', query.lower())
        model = item_list.model()

        for i in config['downloadList'].get(page, {}).get(cat, {}).get('item', []):
            item_id = i.get('id')
            if item_id in queued_ids:
                continue

            name = sanitizer.sub('', i.get('name', '').lower())
            match_found = clean_query in name

            if not match_found and 'altnames' in i:
                match_found = any(
                    clean_query in sanitizer.sub('', alt.lower())
                    for alt in i['altnames']
                )

            if match_found:
                item = DownloadableItem(i['name'])
                item.setAttrs(i, page, cat)
                if item.icon().isNull():
                    item.setIcon(resources.icons.get('blank_24'))
                model.appendRow(item)

    def search(self, query: str):
        clean_query = sanitizer.sub('', query.lower())
        results_model = self.results.item_list.model()
        results_model.clear()

        if not clean_query:
            return

        queued_ids = self._get_queue_ids()

        if self.main and hasattr(self.main, 'sections'):
            for section in self.main.sections:
                self.searchList(section[0], section[1], self.results.item_list, clean_query, queued_ids)

        self._search_checkboxes(clean_query, queued_ids)

        items = [results_model.takeRow(0)[0] for _ in range(results_model.rowCount())]
        items.sort(key=lambda item: item.text().lower())

        for item in items:
            results_model.appendRow(item)

        if results_model.rowCount() == 0:
            placeholder = DownloadableItem(f'No results for "{query}"')
            placeholder.setEnabled(False)
            results_model.appendRow(placeholder)

    def refresh(self):
        self.results.deselectAllItems()
        self.query.textChanged.emit(self.query.text())

    def addSelected(self):
        items = self.results.getSelectedItems()
        queue_model = self.queue.item_list.model()
        existing_ids = self._get_queue_ids()

        for item in items:
            self._add_item_to_queue(item, queue_model, existing_ids)

        self.refresh()

    def removeSelected(self):
        model = self.queue.item_list.model()

        for item in reversed(self.queue.getSelectedItems()):
            model.removeRow(item.row())

        self.refresh()

    def addItem(self, index):
        results_model = self.results.item_list.model()
        item = results_model.item(index.row())
        if item:
            queue_model = self.queue.item_list.model()
            existing_ids = self._get_queue_ids()
            self._add_item_to_queue(item, queue_model, existing_ids)

    def confirm(self):
        queue_model = self.queue.item_list.model()
        old_model = self.oldQueue.model()

        def extract_ids(model):
            ids = set()
            for row in range(model.rowCount()):
                item = model.item(row)
                if item:
                    item_id = model.data(item.index(), ID_ROLE)
                    if item_id:
                        ids.add(item_id)
            return ids

        old_ids = extract_ids(old_model)
        current_ids = extract_ids(queue_model)

        if old_ids == current_ids:
            self.close()
            return

        added_count = len(current_ids - old_ids)
        removed_count = len(old_ids - current_ids)

        info_lines = []
        if added_count > 0:
            info_lines.append(f'{added_count} new item{"s" if added_count > 1 else ""}')
        if removed_count > 0:
            info_lines.append(f'{removed_count} removed item{"s" if removed_count > 1 else ""}')

        msg_box = QMessageBox(self)
        msg_box.setText('Do you want to save your changes?')
        if info_lines:
            msg_box.setInformativeText("\n".join(info_lines))

        msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Cancel)

        item_names = [queue_model.item(i).text() for i in range(queue_model.rowCount()) if queue_model.item(i)]
        msg_box.setDetailedText('Selected items:\n' + '\n'.join(item_names))

        match msg_box.exec():
            case QMessageBox.Save:
                if self.main:
                    for section in self.main.findChildren(DownloadListSection):
                        section.deselectAllItems()

                    for cb in self.main.findChildren(QCheckBox):
                        cb.setChecked(False)

                    for row in range(queue_model.rowCount()):
                        item = queue_model.item(row)
                        if not item:
                            continue

                        if getattr(item, 'is_checkbox', False) or item.text() in self.reverse_checkboxes:
                            real_name = getattr(item, 'real_name', None) or self.reverse_checkboxes.get(item.text())
                            if real_name:
                                cb_widget = self.main.findChild(QCheckBox, name=real_name)
                                if cb_widget:
                                    cb_widget.setChecked(True)
                        else:
                            item_id = queue_model.data(item.index(), ID_ROLE)
                            cat = getattr(item, 'specialAttrs', {}).get('cat') if hasattr(item, 'specialAttrs') else None
                            if cat:
                                sec_widget = self.main.findChild(DownloadListSection, cat)
                                if sec_widget:
                                    sec_widget.selectChild(item_id)

                return True
            case QMessageBox.Discard:
                return True
            case QMessageBox.Cancel:
                return False
