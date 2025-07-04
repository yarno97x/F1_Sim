from PySide6.QtWidgets import QPushButton, QApplication, QMainWindow
from PySide6.QtGui import QFont
from enums import IndicatorType

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

if __name__ == "__main__" :
    app = QApplication()
    window = QMainWindow()

    window.setCentralWidget(Indicator(IndicatorType.DRS))
    window.show()
    app.exec()
