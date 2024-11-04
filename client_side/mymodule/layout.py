from .myclass import button, window
from PySide6.QtWidgets import (QVBoxLayout, QScrollArea, QHBoxLayout, \
                               QTextEdit, QWidget)
from PySide6.QtCore import (Qt, QRect, QSize)

class scrol_child_widget(QWidget) :
    def __init__(self, window : QWidget) :
        super().__init__(window)
        layout = QVBoxLayout() 
        self.button = []
        self.button.append(button("alamak", 100, 200, self))
        self.button.append(button("TEST", 100, 200, self))

        layout.addWidget(self.button[0])
        layout.addWidget(self.button[1])


        self.setLayout(layout)
    def add_button(self, name : str):
        pass


class main_window_layout(QWidget):
    def __init__(self, window: QWidget) :
        super().__init__(window)
        """instances"""
        textcolumn = QTextEdit(None, self) 
        textcolumn.setFixedSize(200,200)

        '''scroll area'''

        scroll_area = QScrollArea(self)
        scroll_area.setGeometry(0, 0 , 100, 500)
        scroll_area.setMinimumSize(QSize(100, 450))
        scroll_area.setFixedWidth(200)


        child_scroll = scrol_child_widget(scroll_area)
        scroll_area.setWidget(child_scroll)
        scroll_area.setWidgetResizable(True)

        """layout"""
        secondlayout =  QVBoxLayout()
        mainlayout = QHBoxLayout()
        mainlayout.addWidget(scroll_area,alignment= Qt.AlignmentFlag.AlignLeft)
        mainlayout.addWidget(textcolumn)
        
        self.setLayout(mainlayout)
        self.setObjectName("window")
 


