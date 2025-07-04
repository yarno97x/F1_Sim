from PySide6.QtWidgets import QPushButton, QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont
from enums import drivers, tracks
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../controller')))
from controller import Controller

class ButtonCard(QPushButton) :
    def __init__(self, obj) :
        self.value = obj.value
        super().__init__(text=self.value["name"])
        font = QFont("Eras Bold ITC", 14)
        self.setFont(font)
        self.setFixedSize(200, 100)

        self.setStyleSheet(f"""
            background-color: rgba({int(self.value["color"][1:3], 16)}, {int(self.value["color"][3:5], 16)}, {int(self.value["color"][5:7], 16)}, 98);
            color: white;
            font-weight: bold;
            border-radius: 5px;
            margin: 10px;
            border: 0px grey solid;
            padding: 5px;
        """)

        self.clicked.connect(self.button_clicked)

    def button_clicked(self) :
        c.choose_driver(self.value["name"])

class ButtonGrid(QWidget) :
    def __init__(self, kind) :
        super().__init__()
        data = drivers if kind == "drivers" else tracks
        width = 5 if kind == "drivers" else 6

        horizontal = QHBoxLayout()
        for i in range(width) :
            vertical = QVBoxLayout()
            for j in range(4) :
                vertical.addWidget(ButtonCard(data[i, j]))
            horizontal.addLayout(vertical)
        self.setLayout(horizontal)
                
if __name__ == "__main__" :
    app = QApplication()
    window = QMainWindow()
    c = Controller()

    window.setCentralWidget(ButtonGrid("drivers"))
    window.show()
    app.exec()
