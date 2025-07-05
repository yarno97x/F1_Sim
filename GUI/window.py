from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QSizePolicy
from components.buttonGrid import ButtonGrid
from pages.start import StartPage
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../controller')))
from controller import Controller

modes = {
    "Navy":       "#001F3F",
    "Red":        "#8B0000",
    "Purple":     "#2E003E",
    "Teal":       "#004D4D",
    "Midnight":   "#191970",
}

class Window(QMainWindow) :
    def __init__(self, app, c, ends = modes["Midnight"], middle = "black") :
        super().__init__()
        self.app = app
        self.set_styles(ends, middle)
        menu = self.menuBar()
        menu.setStyleSheet(f"background-color: {ends}; border: 1px solid white")
        options = menu.addMenu("&Options")
        themes = menu.addMenu("&Themes")
        for theme in modes.keys() :
            action = themes.addAction(f"{theme}")
            action.triggered.connect(lambda checked=False, t=theme: self.change_color(modes[t]))
        
        again = options.addAction("Start Over")
        again.triggered.connect(self.start_again)
        quit = options.addAction("Quit")
        quit.triggered.connect(self.quit_app)

        self.stack = QStackedWidget()

        self.start = StartPage(lambda: self.stack.setCurrentIndex(1))
        self.choose_driver = ButtonGrid("drivers", c, lambda: self.stack.setCurrentIndex(2))
        self.choose_track = ButtonGrid("tracks", c, lambda: self.stack.setCurrentIndex(0))

        self.stack.addWidget(self.start)
        self.stack.addWidget(self.choose_driver)
        self.stack.addWidget(self.choose_track)
        
        self.setCentralWidget(self.stack)

    def set_styles(self, ends, middle) :
        self.setStyleSheet(f"""
            background-color: qlineargradient(
                y1: 0, 
                y2: 1, 
                stop: 0 {ends}, 
                stop: 0.3 {middle},
                stop: 0.9 {middle}, 
                stop: 1 {ends})
            """)
        
    def change_color(self, color) :
        self.menuBar().setStyleSheet(f"background-color: {color}; border: 1px solid white")
        self.setStyleSheet(f"""
            background-color: qlineargradient(
                           y1: 0, 
                           y2: 1, 
                           stop: 0 {color}, 
                           stop: 0.3 "black",
                           stop: 0.9 "black", 
                           stop: 1 {color})
        """)
        print(f"Changing to {color}")

    def quit_app(self) :
        self.app.quit()

    def start_again(self) :
        self.stack.setCurrentIndex(0)
        
if __name__ == "__main__" :
    app = QApplication()
    c = Controller()
    window = Window(app, c)
    window.showMaximized()
    app.exec()
