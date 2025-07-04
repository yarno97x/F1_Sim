from PySide6.QtWidgets import QPushButton, QApplication, QWidget, QLabel, QMainWindow, QVBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class StartPage(QWidget) :
    def __init__(self, switch) :
        super().__init__()
        self.switch = switch
        # self.setStyleSheet("border: 5px solid white")

        layout = QVBoxLayout()

        title = QLabel("F1 TELEMETRY SIMULATOR\n+\nPIT STRATEGY")
        font = QFont("Eras Bold ITC", 14)
        title.setStyleSheet("color: white")

        title.setMinimumSize(300, 100)
        title.setMaximumSize(500, 100)
        title.setFont(font)
        title.setAlignment(Qt.AlignCenter)

        button = QPushButton("Start")
        button.setMinimumSize(100, 50)
        button.setMaximumSize(200, 50)
        button.setFont(font)
        
        layout.addWidget(title, alignment=Qt.AlignCenter)
        layout.addWidget(button, alignment=Qt.AlignCenter)

        layout.setSpacing(1)
        layout.setContentsMargins(100, 100, 100, 100)
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
