import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))
from driver import Driver
from team import Team
from f1_data import F1DriverInfo

class Controller :
    def __init__(self):
        pass

    def choose_driver(self, name) :
        self.driver = Driver(name, F1DriverInfo[name]["number"])
        self.team = Team(F1DriverInfo[name]["team"])
        self.driver.join_team(self.team)
        print(f"Driver -> {self.driver}")

    def choose_track(self, track) :
        self.track = track
        print(f"Track -> {self.track}")
