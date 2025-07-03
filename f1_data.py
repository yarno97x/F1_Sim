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
    
F1Drivers = {
    "Carlos Sainz": 55,
    "Alexander Albon": 23,
    "George Russell": 63,
    "Kimi Antonelli": 12,
    "Lewis Hamilton": 44,
    "Charles Leclerc": 16,
    "Oscar Piastri": 81,
    "Lando Norris": 4,
    "Max Verstappen": 1,
    "Yuki Tsunoda": 22,
    "Liam Lawson": 30,
    "Isack Hadjar": 6,
    "Esteban Ocon": 31,
    "Oliver Bearman": 87,
    "Lance Stroll": 18,
    "Fernando Alonso": 14,
    "Nico Hulkenberg": 27,
    "Gabriel Bortoleto": 5,
    "Pierre Gasly": 10,
    "Franco Colapinto": 43
}
