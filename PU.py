from enum import Enum, auto

class PU_constructors(Enum) :
    MERCEDES = auto()
    REDBULL_FORD = auto()
    FERRARI = auto()
    RENAULT = auto()
    AUDI = auto()
    HONDA = auto()

class PU :
    def __init__(self, constructor):
        if type(constructor) != PU_constructors :
            raise TypeError("PU Constructor not in PU_constructors")

        self.constructor = constructor
        self.top_speed = 340 # km/h

    def __repr__(self) :
        return "[PU]"
