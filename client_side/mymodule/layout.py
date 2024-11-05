from .myclass import button, window
from PySide6.QtWidgets import (QVBoxLayout, QScrollArea, QHBoxLayout, \
                               QTextEdit, QLabel,QWidget)
from PySide6.QtCore import (Qt, QRect, QSize)


class scrol_child_widget(QWidget) :
    def __init__(self, window : QWidget) :
        super().__init__(window)
        self.layout = QVBoxLayout(self) 
        self.button = []

        self.setLayout(self.layout) 

    def add_button(self, name : str):
        self.button.append(button(name, 100, 50))
        self.layout.addWidget(self.button[self.button.index()])

        self.button.append(button(name, 100, 50))
        self.layout.addWidget(self.button[-1])
    
class layout_column(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        layout1 = QVBoxLayout()
        """layout2 = QHBoxLayout()"""

        self.text_column = QTextEdit()
        self.title_label = QLabel()
        self.date_label = QLabel()
        layout2 = QHBoxLayout()
        layout1.addWidget(self.title_label)
        layout1.addWidget(self.date_label)
        layout1.addWidget(self.text_column)
        self.setLayout(layout1)
        self.setObjectName("layoutchild")


class main_window_layout(QWidget):
    def __init__(self, window: QWidget) :
        super().__init__(window)
        """instances"""        
        title_label= QLabel()
        date_label = QLabel()
        textcolumn = QTextEdit(None, self) 
        textcolumn.setMinimumSize(200,200)

        '''scroll area'''

        scroll_area = QScrollArea(self)
        scroll_area.setGeometry(0, 0 , 200, 500)
        scroll_area.setMinimumSize(QSize(200, 450))
        scroll_area.setFixedWidth(200)


        child_scroll = scrol_child_widget(scroll_area)
        scroll_area.setWidget(child_scroll)
        scroll_area.setWidgetResizable(True)

        """layout"""
        thirdlayout = QHBoxLayout()
        secondlayout =  QVBoxLayout()
        mainlayout = QHBoxLayout()
        mainlayout.addWidget(scroll_area,alignment= Qt.AlignmentFlag.AlignLeft)
        layoutcolumn = layout_column(self)
        mainlayout.addWidget(layoutcolumn)
        
        self.setLayout(mainlayout)
        self.setObjectName("window")

    
 


