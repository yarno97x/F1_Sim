from PU import *
from tire import *
from fuel import FuelTank

class Car :
    def __init__(self, power_unit, tires, fuel_tank):
        if not isinstance(power_unit, PU) :
            raise TypeError("Not a power unit")
        if not isinstance(tires, list) or len(tires) != 4 :
            raise TypeError("Not a list of 4 tires")
        if not isinstance(fuel_tank, FuelTank) :
            raise TypeError("Not a a fuel tank")
        elif any([not isinstance(tire, Tire) for tire in tires]) :
            raise TypeError("tires should be a list of <Tire>")
        
        self.power_unit = power_unit
        self.tires = tires
        self.fuel_tank = fuel_tank
        self.DRS = False
    
    def status(self):
        lines = []
        lines.append(f"{self.tires[0]}{' ' * 11}{self.tires[1]}")
        lines.append(f"{8 * ' '}{self.power_unit}{8 * ' '}")
        lines.append(f"{5 * ' '}{self.fuel_tank}{5 * ' '}")
        lines.append(f"{self.tires[2]}{' ' * 11}{self.tires[3]}")
        lines.append(f"{5 * ' '}DRS {'Enabled' if self.DRS else 'Disabled'}")

        centered = "\n".join(lines)
        return centered


    
