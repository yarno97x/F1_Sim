import sys
import os
import pytest, random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model')))
from driver import Driver
from f1_data import F1Team
from team import Team

@pytest.fixture
def carlos():
    return Driver("Carlos Sainz", 55)

@pytest.fixture
def alex() :
    return Driver("Alex Albon", 23)

@pytest.fixture
def lando():
    return Driver("Lando Norris", 4)

@pytest.fixture
def oscar():
    return Driver("Oscar Piastri", 81)

@pytest.fixture
def williams():
    return Team(F1Team.WILLIAMS)

@pytest.fixture
def mclaren():
    return Team(F1Team.MCLAREN)

@pytest.fixture
def random_team() :
    return Team(random.choice(list(F1Team)))

def test_add_one_driver(carlos, williams) :
    williams.add_driver(carlos)
    assert len(williams.drivers) == 1

def test_add_two_drivers(oscar, lando, mclaren) :
    mclaren.add_driver(oscar)
    mclaren.add_driver(lando)
    assert len(mclaren.drivers) == 2

def test_add_three_drivers(oscar, lando, carlos, mclaren) :
    mclaren.add_driver(oscar)
    mclaren.add_driver(lando)
    with pytest.raises(ValueError) :
        mclaren.add_driver(carlos)

def test_remove_driver_with_no_drivers(carlos, williams) :
    with pytest.raises(ValueError) :
        williams.remove_driver(carlos)

def test_remove_existing_driver(carlos, williams) :
    williams.add_driver(carlos)
    williams.remove_driver(carlos)
    assert len(williams.drivers) == 0

def test_remove_existing_driver_2(carlos, alex, williams) :
    williams.add_driver(carlos)
    williams.add_driver(alex)
    williams.remove_driver(carlos)
    assert len(williams.drivers) == 1

def test_remove_existing_drivers(carlos, alex, williams) :
    williams.add_driver(carlos)
    williams.add_driver(alex)
    assert len(williams.drivers) == 2

    williams.remove_driver(alex)
    assert len(williams.drivers) == 1

    williams.remove_driver(carlos)
    assert len(williams.drivers) == 0

def test_hex_codes_are_int(random_team) :
    assert isinstance(random_team.get_primary_color(), int)
    assert isinstance(random_team.get_secondary_color(), int)
