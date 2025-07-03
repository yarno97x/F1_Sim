import random

class FuelTank :
    def __init__(self, fuel = 145):
        self.capacity = 145 # L
        self.fuel = fuel

    def use_fuel(self, track_part_baseline = 1) :
        self.fuel = max(self.total - track_part_baseline * abs(random.gauss(mu=1, sigma=1)), 0)

    def __repr__(self) :
        return f"Fuel Tank [{self.fuel / self.capacity * 100:.1f}%]"
    


