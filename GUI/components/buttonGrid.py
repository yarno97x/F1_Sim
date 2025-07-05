# PySide Imports
from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont

# Imports outside folder
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data')))
from data import drivers, tracks, F1DriverInfo, F1TrackInfo

class ButtonCard(QPushButton) :
    def __init__(self, name, color, controller, switch) :
        self.c = controller
        self.switch = switch

        self.name, self.color = name, color
        if name in F1DriverInfo.keys() :
            self.kind = "driver"
            name = name + "\n" + F1DriverInfo[name]["team"].name
        else :
            self.kind = "track"
            name = name + "\n" + F1TrackInfo[name]["country"]
        super().__init__(name.replace("_", " "))
        font = QFont("Eras Bold ITC", 14)
        self.setFont(font)
        self.setMinimumSize(200, 100)
        self.setMaximumSize(400, 150)

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: rgba({int(self.color[1:3], 16)}, {int(self.color[3:5], 16)}, {int(self.color[5:7], 16)}, 98);
                color: white;
                font-weight: bold;
                border-radius: 5px;
                margin: 10px;
                border: 0px grey solid;
                padding: 5px;
            }}
            QPushButton:hover {{
                background-color: blue;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                margin: 10px;
                border: 1px solid white;
                padding: 5px;
            }}

            QPushButton:pressed {{
                background-color: white;
                color: black;
                font-weight: bold;
                border-radius: 5px;
                margin: 10px;
                border: 1px solid white;
                padding: 5px;
            }}
        """)

        self.clicked.connect(self.button_clicked)

    def button_clicked(self) :
        # print(type(self.value))
        # print(self.value)
        if self.kind == "driver" :
            self.c.choose_driver(self.name)
        else :
            self.c.choose_track(self.name)
        self.switch()

class ButtonGrid(QWidget) :
    def __init__(self, kind, controller, switch) :
        super().__init__()
        data = drivers if kind == "drivers" else tracks
        width = 5 if kind == "drivers" else 6

        horizontal = QHBoxLayout()
        for i in range(width) :
            vertical = QVBoxLayout()
            for j in range(4) :
                # print(data[i, j])
                vertical.addWidget(ButtonCard(data[i, j, 0], data[i, j, 1], controller=controller, switch=switch))
            horizontal.addLayout(vertical)
        self.setLayout(horizontal)
                