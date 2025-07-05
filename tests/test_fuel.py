import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model')))
from fuel import FuelTank

def test_has_realistic_amount_of_fuel() :
    tank = FuelTank()
    assert hasattr(tank, "fuel") and tank.fuel <= 145 and tank.fuel > 0
