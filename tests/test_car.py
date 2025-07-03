import pytest
import sys
import os, random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PU import PU, PU_constructors
from tire import *
from fuel import FuelTank
from car import *

@pytest.fixture
def power_unit() :
    return PU(random.choice(list(PU_constructors)))

@pytest.fixture
def tires() :
    tire_kind = random.choice([Soft, Medium, Hard, Inter, Wet])
    return [tire_kind() for _ in range(4)]

@pytest.fixture
def fuel_tank() :
    return FuelTank()

@pytest.fixture
def car(power_unit, tires, fuel_tank) :
    return Car(power_unit=power_unit, tires=tires, fuel_tank=fuel_tank)

def test_has_all_attributes(car) :
    assert hasattr(car, "power_unit")
    assert hasattr(car, "tires")
    assert hasattr(car, "fuel_tank")
    assert hasattr(car, "DRS")
    assert not car.DRS 

def test_power_unit_error(tires, fuel_tank) :
    with pytest.raises(TypeError) :
        Car(1, tires, fuel_tank)
    with pytest.raises(TypeError) :
        Car("1", tires, fuel_tank)
    with pytest.raises(TypeError) :
        Car([], tires, fuel_tank)

def test_tires_error(power_unit, fuel_tank) :
    with pytest.raises(TypeError) :
        Car(power_unit, 1, fuel_tank)
    with pytest.raises(TypeError) :
        Car(power_unit, "1", fuel_tank)
    with pytest.raises(TypeError) :
        Car(power_unit, [], fuel_tank)

def test_fuel_tank_error(power_unit, tires) :
    with pytest.raises(TypeError) :
        Car(power_unit, tires, 1)
    with pytest.raises(TypeError) :
        Car(power_unit, tires, "1")
    with pytest.raises(TypeError) :
        Car(power_unit, tires, [])
