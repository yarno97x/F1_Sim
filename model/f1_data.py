from enum import Enum

class F1Team(Enum):
    MERCEDES       = (0x00D2BE, 0x000000)  # Teal & Black
    RED_BULL       = (0x1E3A8A, 0x000000)  # Navy Blue & Black
    FERRARI        = (0xDC0000, 0x000000)  # Ferrari Red & Black
    MCLAREN        = (0xFF8700, 0x00C3E0)  # Papaya Orange & Blue
    ASTON_MARTIN   = (0x006F62, 0x000000)  # Racing Green & Black
    ALPINE         = (0x0090FF, 0xFF87BC)  # Blue & Pink (BWT)
    WILLIAMS       = (0x005AFF, 0x000000)  # Blue & Black
    RB             = (0xFFFFFF, 0x005AFF)  # White & Blue
    KICK_SAUBER    = (0x52E252, 0x000000)  # Green & Black
    HAAS           = (0xB6BABD, 0xE10600)  # Silver-Grey & Red

    def primary(self):
        return self.value[0]

    def secondary(self):
        return self.value[1]
    
F1Driver = {
    "Carlos Sainz":        {"number": 55, "team": F1Team.WILLIAMS},
    "Alex Albon":     {"number": 23, "team": F1Team.WILLIAMS},
    "George Russell":      {"number": 63, "team": F1Team.MERCEDES},
    "Kimi Antonelli":      {"number": 12, "team": F1Team.MERCEDES},
    "Lewis Hamilton":      {"number": 44, "team": F1Team.FERRARI},
    "Charles Leclerc":     {"number": 16, "team": F1Team.FERRARI},
    "Oscar Piastri":       {"number": 81, "team": F1Team.MCLAREN},
    "Lando Norris":        {"number": 4,  "team": F1Team.MCLAREN},
    "Max Verstappen":      {"number": 1,  "team": F1Team.RED_BULL},
    "Yuki Tsunoda":        {"number": 22, "team": F1Team.RED_BULL},
    "Liam Lawson":         {"number": 30, "team": F1Team.RB},
    "Isack Hadjar":        {"number": 6,  "team": F1Team.RB},
    "Esteban Ocon":        {"number": 31, "team": F1Team.HAAS},
    "Oliver Bearman":      {"number": 87, "team": F1Team.HAAS},
    "Lance Stroll":        {"number": 18, "team": F1Team.ASTON_MARTIN},
    "Fernando Alonso":     {"number": 14, "team": F1Team.ASTON_MARTIN},
    "Nico Hulkenberg":     {"number": 27, "team": F1Team.KICK_SAUBER},
    "Gabriel Bortoleto":   {"number": 5,  "team": F1Team.KICK_SAUBER},
    "Pierre Gasly":        {"number": 10, "team": F1Team.ALPINE},
    "Franco Colapinto":    {"number": 43, "team": F1Team.ALPINE},
}

