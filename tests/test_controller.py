import pytest, sys, os, random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../controller')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))
from data import F1DriverInfo
from controller import Controller

@pytest.fixture
def random_driver() :
    return random.choice(list(F1DriverInfo.keys()))

@pytest.fixture
def controller() :
    return Controller()

def test_add_random_driver(controller, random_driver) :
    controller.choose_driver(random_driver)
    assert controller.driver.name == random_driver
