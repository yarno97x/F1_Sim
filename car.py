from PU import PU
from tire import *
from fuel import FuelTank

class Car :
    def __init__(self, power_unit, tires, fuel_tank):
        if any([not isinstance(power_unit, PU), not isinstance(tires, list), not isinstance(fuel_tank, FuelTank)]) :
            raise TypeError("Car inputs not well formatted")
        elif any([not isinstance(tire, Tire) for tire in tires]) :
            raise TypeError("tires should be a list of <Tire>")
        
        self.PU = PU
        self.tires = tires
        self.fuel_tank = fuel_tank
        self.DRS = False

    def get_tire_temperatures(self) :
        return [tire.temperature for tire in self.tires]
    
