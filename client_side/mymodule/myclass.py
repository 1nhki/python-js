from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QListWidget, QPushButton
)


class window (QWidget):
    def __init__(self,title : str,  parent: QWidget | None = ..., \
                 f: Qt.WindowType = ... , ) -> None:
        super().__init__(parent,Qt.Window)
        self.setWindowTitle(f"{title}")
        self.setFixedSize(100, 100)

    def setsize (self, size : list):
        self.setFixedSize(size[0], size[1])

class button(QPushButton):
    def __init__(self, strings : str, height : int , width : int, parent = ...) -> None:
        super().__init__(strings, parent)
        self.setFixedSize(width, height)
        self.setStyleSheet("")