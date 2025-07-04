import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model')))

from team import Team
from f1_data import F1Team
from driver import Driver

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

def test_add_driver(carlos, williams) :
    carlos.join_team(williams)
    assert carlos.team == williams

def test_add_driver_error(carlos, williams, mclaren) :
    carlos.join_team(williams)
    with pytest.raises(ValueError) :
        carlos.join_team(mclaren)

def test_change_teams(carlos, mclaren, williams) :
    carlos.join_team(williams)
    assert carlos.team == williams
    carlos.change_team(mclaren)
    assert carlos.team == mclaren

def test_quit_empty_team(carlos) :
    with pytest.raises(ValueError) :
        carlos.leave_team()

def test_quit_team(carlos, williams) :
    carlos.join_team(williams)
    assert carlos.team == williams

    carlos.leave_team()
    assert not carlos.team 

