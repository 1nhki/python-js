from .myclass import button, window
from PySide6.QtWidgets import (QVBoxLayout, QScrollArea, QHBoxLayout, \
                               QTextEdit, QWidget)
from PySide6.QtCore import (Qt, QRect, QSize)

class main_window_layout():
    def __init__(self, window: QWidget) :
        
        """instances"""
        Button = []
        Button.append(button("catch", 20, 20 ))
        Button.append(button("back", 20, 20 )) 

        textcolumn = QTextEdit(None, window) 
        textcolumn.setFixedSize(100,100)

        '''scroll area'''
        scroll_area = QScrollArea(window)
        scroll_area.setFixedSize(100,200)
        scroll_area_layout = QVBoxLayout()
        scroll_area.setLayout(scroll_area_layout)
        scroll_area.setWidget(Button[0])
        scroll_area.setWidget(Button[1])

        """layout"""
        secondlayout =  QVBoxLayout()
        secondlayout.addWidget(textcolumn)
        mainlayout = QHBoxLayout()
        mainlayout.addWidget(scroll_area)
        mainlayout.addLayout(secondlayout)


