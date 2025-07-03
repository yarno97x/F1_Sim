from enum import Enum, auto

class Compound(Enum):
    C1 = "C1"
    C2 = "C2"
    C3 = "C3"
    C4 = "C4"
    C5 = "C5"

class TireCategory(Enum):
    HARD = [Compound.C1, Compound.C2]
    MEDIUM = [Compound.C3]
    SOFT = [Compound.C4, Compound.C5]

class Tire :
    def __init__(self):
        self.life = 100

class Slick(Tire) :
    def __init__(self):
        super().__init__()

class Soft(Slick) :
    def __init__(self):
        super().__init__()
        self.color = 0xFF4444

class Medium(Slick) :
    def __init__(self):
        super().__init__()
        self.color = 0xFFD700

class Hard(Slick) :
    def __init__(self):
        super().__init__()
        self.color = 0xE0E0E0

class Inter(Tire) :
    def __init__(self):
        super().__init__()
        self.color = 0x33FF33

class Wet(Tire) :
    def __init__(self):
        super().__init__() 
        self.color = 0x3399FF
