import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model')))
from driver import Driver
from team import Team
from f1_data import *

class Controller :
    def __init__(self):
        pass

    def choose_driver(self, name) :
        self.driver = Driver(name, F1Driver[name]["number"])
        self.team = Team(F1Driver[name]["team"])
        self.driver.join_team(self.team)
