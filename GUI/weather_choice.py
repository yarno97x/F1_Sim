from PySide6.QtWidgets import QPushButton, QApplication, QWidget, QCheckBox
from PySide6.QtGui import QFont

class WeatherPage(QWidget) :
    def __init__(self, controller, switch) :
        super().__init__()

