from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QFont
from enum import Enum

class IndicatorType(Enum) :
    DRS = {"text" : "DRS", "color" : "#00B050"}
    OUT = {"text" : "OUT", "color" : "#4E95D9"}
    PIT = {"text" : "PIT", "color" : "#FF0000"}

class Indicator(QPushButton) :
    def __init__(self, indicator_type) :
        super().__init__(indicator_type.value["text"])
        font = QFont("Eras Bold ITC", 14)
        self.setFont(font)
        self.setFixedSize(120, 40)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {indicator_type.value["color"]};
                color: white;
                font-weight: bold;
                border-radius: 10px;
                border: 0px grey solid;
                padding: 8px;
            }}
        """)
        self.setCheckable(True)
        self.clicked.connect(self.toggle_button)
        self.off = True
        self.indicator_type = indicator_type

    def toggle_button(self) :
        color = self.indicator_type.value["color"] if not self.off else "transparent"
        border = "none" if not self.off else "1px solid lightgray"
        text_color = "grey" if self.off else "white"
        self.off = not self.off
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                font-weight: bold;
                border-radius: 10px;
                border: {border};
                padding: 8px;
                color: {text_color}
            }}
        """)

class Indicators(QWidget) :
    def __init__(self, orientation = "horizontal") :
        super().__init__()
        if orientation == "horizontal" :
            self.layout = QHBoxLayout()
        else :
            self.layout = QVBoxLayout()
        
        for indicator in list(IndicatorType) :
            self.layout.addWidget(Indicator(indicator))
        self.setLayout(self.layout)
        
        if orientation == "horizontal" :
            self.setFixedSize(200, 150)
        else :
            self.setFixedSize(150, 200)
        self.setMinimumSize(150, 100)
        self.setMaximumSize(400, 300)
        self.setStyleSheet("border: 10px solid white;")

