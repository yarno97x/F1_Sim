from f1_data import F1Team

class Driver :
    def __init__(self, name, number):
        if not isinstance(name, str) or not isinstance(number, int) :
            raise TypeError("Name should be a str, number should be an int")
        
        self.name = name
        self.number = number
        self.team = None

    def join_team(self, team) :
        if self.team :
            raise ValueError(f"{self} already is at {self.team}")
        self.team = team
        if self not in team.drivers :
            team.add_driver(self)

    def change_team(self, team) :
        if len(team.drivers) == 2 :
            raise ValueError("Cannot add third driver to team")
        self.team = team
        if self not in team.drivers :
            team.add_driver(self)

    def leave_team(self) :
        if not self.team :
            raise ValueError("Cannot quit null team")
        team = self.team
        self.team = None
        if self in team.drivers :
            team.remove_driver(self)

    def __repr__(self):
        return f"{self.name} [{self.number}] at {self.team.name if self.team else ''}"
