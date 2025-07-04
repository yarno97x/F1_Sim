import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model')))

from tire import *

@pytest.fixture
def soft() :
    return Soft()

@pytest.fixture
def medium() :
    return Medium()

@pytest.fixture
def hard() :
    return Hard()

@pytest.fixture
def inter() :
    return Inter()

@pytest.fixture
def wet() :
    return Wet()

@pytest.fixture 
def random_slick() :
    return random.choice([Soft, Medium, Hard])()

@pytest.fixture
def random_tire() :
    return random.choice([Soft, Medium, Hard, Inter, Wet])()

def test_tire_creation() :
    for kind in [Soft, Medium, Hard, Inter, Wet] :
        x = kind()
        assert (hasattr(x, "life") and hasattr(x, "color"))

def test_tire_colors() :
    colors = {
        Soft : 0xFF4444, 
        Medium : 0xFFD700, 
        Hard : 0xE0E0E0, 
        Inter : 0x33FF33, 
        Wet : 0x3399FF
    }

    for kind, hex in colors.items():
        x = kind()
        assert hasattr(x, "color") and x.color == hex

def test_has_temperature(random_tire) :
    assert hasattr(random_tire, "temperature")

def test_soft_temp_range(soft) :
    assert 110 >= soft.temperature >= 90

def test_med_temp_range(medium) :
    assert 120 >= medium.temperature >= 100

def test_hard_temp_range(hard) :
    assert 130 >= hard.temperature >= 110

def test_inter_temp_range(inter) :
    assert 80 >= inter.temperature >= 60

def test_wet_temp_range(wet) :
    assert 70 >= wet.temperature >= 50

def test_has_compound(random_tire) :
    assert hasattr(random_tire, "compound")

def test_soft_wrong_compound() :
    with pytest.raises(ValueError) :
        Soft(compound=Compound.C3)
    with pytest.raises(ValueError) :
        Soft(compound=Compound.C2)
    with pytest.raises(ValueError) :
        Soft(compound=Compound.C1)

def test_medium_wrong_compound() :
    with pytest.raises(ValueError) :
        Medium(compound=Compound.C5)
    with pytest.raises(ValueError) :
        Medium(compound=Compound.C4)
    with pytest.raises(ValueError) :
        Medium(compound=Compound.C2)
    with pytest.raises(ValueError) :
        Medium(compound=Compound.C1)

def test_hard_wrong_compound() :
    with pytest.raises(ValueError) :
        Hard(compound=Compound.C5)
    with pytest.raises(ValueError) :
        Hard(compound=Compound.C4)
    with pytest.raises(ValueError) :
        Hard(compound=Compound.C3)

