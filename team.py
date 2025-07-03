from driver import *
from f1_data import F1Team

class Team :
    def __init__(self, name = None):
        if not isinstance(name, F1Team) :
            raise ValueError("Not a team")
        self.name = name
        self.drivers = []

    def add_driver(self, driver) :
        if (len(self.drivers) < 2) :
            self.drivers.append(driver)
            
            if driver.team != self :
                driver.join_team(self)
            return True
        else :
            raise ValueError("Cannot add more than 2 race drivers to a team.")
        
    def remove_driver(self, driver) :
        if driver in self.drivers :
            self.drivers.remove(driver)
            if driver.team == self :
                driver.leave_team()
            return True
        else :
            raise ValueError("Driver not found")
    
    def get_primary_color(self) :
        return self.name.primary()
    
    def get_secondary_color(self) :
        return self.name.secondary()
    
    def __repr__(self) :
        return f"{self.name} {self.drivers}"

