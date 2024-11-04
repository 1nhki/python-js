from PySide6.QtCore import (Qt, QRect, QSize)
from PySide6.QtWidgets import (
    QWidget, QListWidget, QPushButton, QMainWindow
)


class window (QMainWindow):
    def __init__(self,title : str,  parent: QWidget | None = None,\
                 f: Qt.WindowType = ... , ) -> None:
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumSize(500, 500)
        
    def child(self, child : QWidget):
        self.setCentralWidget(child)

    def setsize (self, size : list):
        self.resize(size[0], size[1])



class button(QPushButton):
    def __init__(self, strings : str, height : int , width : int, parent = None ) -> None:
        super().__init__(strings, parent)
        self.setFixedSize(width, height)
        self.setStyleSheet("")


