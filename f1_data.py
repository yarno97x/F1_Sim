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
