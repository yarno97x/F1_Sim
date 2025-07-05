from PySide6.QtWidgets import QPushButton, QApplication, QWidget, QLabel, QMainWindow, QVBoxLayout, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class StartPage(QWidget) :
    def __init__(self, switch) :
        super().__init__()
        self.switch = switch

        layout = QVBoxLayout()

        title = QLabel("F1 TELEMETRY SIMULATOR\n+\nPIT STRATEGY")
        font = QFont("Eras Bold ITC", 16)
        title.setStyleSheet("color: white; background-color: black; border: 3px solid white")

        title.setMinimumSize(300, 100)
        title.setMaximumSize(500, 100)
        title.setFont(font)
        title.setAlignment(Qt.AlignCenter)

        button = QPushButton("Start")
        button.setMinimumSize(100, 50)
        button.setMaximumSize(200, 50)
        button.setFont(font)
        button.setStyleSheet("border: 3px solid white")
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        layout.addWidget(title, alignment=Qt.AlignCenter)
        layout.addWidget(button, alignment=Qt.AlignCenter)

        layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.setLayout(layout)

        button.clicked.connect(self.start)

    def start(self) :
        self.switch()

if __name__ == "__main__" :
    app = QApplication()
    window = QMainWindow()
    start = StartPage()
    window.setCentralWidget(start)
    window.show()
    app.exec()
