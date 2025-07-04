from enum import Enum
import random

RESET = "\033[0m"

class Compound(Enum):
    C1 = "C1"
    C2 = "C2"
    C3 = "C3"
    C4 = "C4"
    C5 = "C5"
    I = "I"
    W = "W"

class TireCategory(Enum):
    HARD = [Compound.C1, Compound.C2]
    MEDIUM = [Compound.C3]
    SOFT = [Compound.C4, Compound.C5]

class Tire :
    def __init__(self, temperature, compound):
        self.life = 100
        self.temperature = temperature
        self.compound = compound

class Slick(Tire) :
    def __init__(self, temperature, compound):
        super().__init__(temperature=temperature, compound=compound)

class Soft(Slick) :
    def __init__(self, compound = Compound.C5):
        if compound not in TireCategory.SOFT.value :
            raise ValueError("Wrong compound")
        super().__init__(temperature = random.uniform(90, 110), compound = compound)
        self.color = 0xFF4444
    
    def __repr__(self) :
        return f"{'\033[91m'} [X] {RESET}"

class Medium(Slick) :
    def __init__(self, compound = Compound.C3):
        if compound not in TireCategory.MEDIUM.value :
            raise ValueError("Wrong compound")
        super().__init__(temperature = random.uniform(100, 120), compound = compound)
        self.color = 0xFFD700
    
    def __repr__(self) :
        return f"{'\033[93m'} [X] {RESET}"

class Hard(Slick) :
    def __init__(self, compound = Compound.C1):
        if compound not in TireCategory.HARD.value :
            raise ValueError("Wrong compound")
        super().__init__(temperature = random.uniform(110, 130), compound = compound)
        self.color = 0xE0E0E0
    
    def __repr__(self) :
        return f"{'\033[97m'} [X] {RESET}"

class Inter(Tire) :
    def __init__(self):
        super().__init__(temperature = random.uniform(60, 80), compound=Compound.I)
        self.color = 0x33FF33

    def __repr__(self) :
        return f"{'\033[92m'} [X] {RESET}"

class Wet(Tire) :
    def __init__(self):
        super().__init__(temperature = random.uniform(50, 70), compound=Compound.W) 
        self.color = 0x3399FF
    
    def __repr__(self) :
        return f"{'\033[94m'} [X] {RESET}"

