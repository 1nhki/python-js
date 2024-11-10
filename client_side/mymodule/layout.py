from .myclass import button, window
from PySide6.QtWidgets import (QVBoxLayout, QScrollArea, QHBoxLayout, \
                               QTextEdit, QLabel,QWidget)
from PySide6.QtCore import (Qt, QRect, QSize)

import requests
import json

notesa = requests.get("http://localhost:5000/notes")
test = json.loads(notesa.text)
print(test)



class scrol_child_widget(QWidget) :
    def __init__(self, window : QWidget) :
        super().__init__(window)
        self.layout = QVBoxLayout(self) 
        self.button = []

        self.setLayout(self.layout) 

    def add_button(self, name : str):
        self.button.append(button(name, 100, 150))
        self.layout.addWidget(self.button[-1])
    
class layout_column(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        layout1 = QVBoxLayout()
        self.layout2 = QVBoxLayout()
        """self.layout2 = QHBoxLayout()"""

        self.container1= QWidget(self)
        self.container1.setLayout(layout1)
        self.newnotes = button("add new", 50, 100, self)
        self.newnotes.clicked.connect(self.toggle)
        layout1.addWidget(self.newnotes, alignment= Qt.AlignmentFlag.AlignCenter)

        self.container3 = QWidget(self)
        self.container3.setLayout(self.layout2)
        self.text_column = QTextEdit()
        self.title_label = QLabel()
        self.title_label.setText("Title")
        self.title_label.setStyleSheet("font-size : 32px")
        self.date_label = QLabel("LOREM IPSUM")
        button_add = button("add", 60, 100, self)

        self.layout2.addWidget(self.title_label)
        self.layout2.addWidget(self.date_label)
        self.layout2.addWidget(self.text_column)
        self.layout2.addWidget(button_add)
        """ self.setLayout(layout1)"""
        self.container3.setVisible(False)
        self.setObjectName("layoutchild")   

    def toggle(self):
        self.container1.setVisible(False)
        self.container3.setVisible(True)
        self.setLayout(self.layout2)

class main_window_layout(QWidget):
    def __init__(self, window: QWidget) :
        super().__init__(window)

        '''scroll area'''

        scroll_area = QScrollArea(self)
        scroll_area.setGeometry(0, 0 , 200, 500)
        scroll_area.setMinimumSize(QSize(200, 450))
        scroll_area.setFixedWidth(200)


        child_scroll = scrol_child_widget(scroll_area)
        if len(test["data"]["notes"]) != 0 :
            for i in test["data"]["notes"]:
                child_scroll.add_button(i["title"])

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

    
 


