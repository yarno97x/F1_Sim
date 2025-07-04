from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from buttonGrid import ButtonGrid
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../controller')))
from controller import Controller

modes = {
    "Navy":       "#001F3F",
    "Red":        "#8B0000",
    "Green":      "#013220",
    "Purple":     "#2E003E",
    "Teal":       "#004D4D",
    "Gray":       "#2F4F4F",
    "Maroon":     "#800000",
    "Indigo":     "#1A1A80",
    "Olive":      "#3D3D00",
    "Chocolate":  "#4B1E00",
    "Midnight":   "#191970",
}


class Window(QMainWindow) :
    def __init__(self, app, c, ends = modes["Midnight"], middle = "black") :
        super().__init__()
        self.app = app
        self.set_styles(ends, middle)

        self.stack = QStackedWidget()

        self.choose_driver = ButtonGrid("drivers", c, lambda: self.stack.setCurrentIndex(1))
        self.choose_track = ButtonGrid("tracks", c, lambda: self.stack.setCurrentIndex(0))

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
        menu = self.menuBar()
        menu.setStyleSheet(f"background-color: {ends}; border: 1px solid white")
        options = menu.addMenu("&Options")
        themes = menu.addMenu("&Themes")
        for theme in modes.keys() :
            action = themes.addAction(f"{theme}")
            action.triggered.connect(lambda checked=False, t=theme: self.change_color(modes[t]))
        quit = options.addAction("Quit")
        quit.triggered.connect(self.quit_app)

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
        
if __name__ == "__main__" :
    app = QApplication()
    c = Controller()
    window = Window(app, c)
    window.show()
    app.exec()
