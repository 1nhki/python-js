from PySide6.QtCore import (Qt, QRect, QSize)
from PySide6.QtWidgets import (
    QWidget, QListWidget, QPushButton
)


class window (QWidget):
    def __init__(self,title : str,  parent: QWidget | None = None, \
                 f: Qt.WindowType = ... , ) -> None:
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(100, 100)

    def setsize (self, size : list):
        self.setFixedSize(size[0], size[1])

class button(QPushButton):
    def __init__(self, strings : str, height : int , width : int, parent = None ) -> None:
        super().__init__(strings, parent)
        self.setFixedSize(width, height)
        self.setStyleSheet("")

