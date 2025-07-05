from PySide6.QtWidgets import QWidget

class Simulation_Page(QWidget) :
    def __init__(self, controller, pages) :
        super().__init__()
        self.c = controller
        self.pages = pages


