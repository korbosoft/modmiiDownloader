# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QSize, Signal
from PySide6.QtWidgets import QTabBar, QTabWidget, QStatusBar

class ClickableStatusBar(QStatusBar):
    clicked = Signal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

class CustomTabWidget(QTabWidget):
    class CustomTabBar(QTabBar):
        def tabSizeHint(self, index: int) -> QSize:
            standard_size = super().tabSizeHint(index)
            tab_count = self.count()

            if tab_count == 0: return standard_size

            fm = self.fontMetrics()

            total_minimum_width = 0
            for i in range(tab_count):
                text_w = fm.horizontalAdvance(self.tabText(i))
                icon_w = self.iconSize().width() + 8 if not self.tabIcon(i).isNull() else 0
                total_minimum_width += (text_w + icon_w)

            remaining_width = self.width() - total_minimum_width

            additional_width = int(remaining_width / tab_count) if remaining_width > 0 else 0

            current_text_w = fm.horizontalAdvance(self.tabText(index))
            current_icon_w = self.iconSize().width() + 8 if not self.tabIcon(index).isNull() else 0

            final_width = current_text_w + current_icon_w + additional_width

            return QSize(final_width, standard_size.height())

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabBar(self.CustomTabBar())