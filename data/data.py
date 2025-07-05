from enum import Enum
import numpy as np

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
    
F1DriverInfo = {
    "Carlos Sainz":      {"number": 55, "team": F1Team.WILLIAMS,     "color": "#005AFF"},
    "Alex Albon":        {"number": 23, "team": F1Team.WILLIAMS,     "color": "#005AFF"},
    "George Russell":    {"number": 63, "team": F1Team.MERCEDES,     "color": "#00D2BE"},
    "Kimi Antonelli":    {"number": 12, "team": F1Team.MERCEDES,     "color": "#00D2BE"},
    "Lewis Hamilton":    {"number": 44, "team": F1Team.FERRARI,      "color": "#DC0000"},
    "Charles Leclerc":   {"number": 16, "team": F1Team.FERRARI,      "color": "#DC0000"},
    "Oscar Piastri":     {"number": 81, "team": F1Team.MCLAREN,      "color": "#FF8700"},
    "Lando Norris":      {"number": 4,  "team": F1Team.MCLAREN,      "color": "#FF8700"},
    "Max Verstappen":    {"number": 1,  "team": F1Team.RED_BULL,     "color": "#1E41FF"},
    "Yuki Tsunoda":      {"number": 22, "team": F1Team.RED_BULL,     "color": "#1E41FF"},
    "Liam Lawson":       {"number": 30, "team": F1Team.RB,           "color": "#6692FF"},
    "Isack Hadjar":      {"number": 6,  "team": F1Team.RB,           "color": "#6692FF"},
    "Esteban Ocon":      {"number": 31, "team": F1Team.HAAS,         "color": "#B6BABD"},
    "Oliver Bearman":    {"number": 87, "team": F1Team.HAAS,         "color": "#B6BABD"},
    "Lance Stroll":      {"number": 18, "team": F1Team.ASTON_MARTIN, "color": "#006F62"},
    "Fernando Alonso":   {"number": 14, "team": F1Team.ASTON_MARTIN, "color": "#006F62"},
    "Nico Hulkenberg":   {"number": 27, "team": F1Team.KICK_SAUBER,  "color": "#66994D"},
    "Gabriel Bortoleto": {"number": 5,  "team": F1Team.KICK_SAUBER,  "color": "#66994D"},
    "Pierre Gasly":      {"number": 10, "team": F1Team.ALPINE,       "color": "#0090FF"},
    "Franco Colapinto":  {"number": 43, "team": F1Team.ALPINE,       "color": "#0090FF"},
}

F1TrackInfo = {
    "MELBOURNE":   {"name": "MELBOURNE", "color": "#00008B", "country": "Australia"},
    "SHANGHAI":    {"name": "SHANGHAI", "color": "#FF0000", "country": "China"},
    "SUZUKA":      {"name": "SUZUKA", "color": "#BC002D", "country": "Japan"},
    "SAKHIR":      {"name": "SAKHIR", "color": "#D71A28", "country": "Bahrain"},
    "JEDDAH":      {"name": "JEDDAH", "color": "#006C35", "country": "Saudi Arabia"},

    "MIAMI":       {"name": "MIAMI", "color": "#3C3B6E", "country": "United States"},
    "IMOLA":       {"name": "IMOLA", "color": "#008C45", "country": "Italy"},
    "MONACO":      {"name": "MONACO", "color": "#ED1C24", "country": "Monaco"},
    "BARCELONA":   {"name": "BARCELONA", "color": "#AA151B", "country": "Spain"},
    "MONTREAL":    {"name": "MONTREAL", "color": "#FF0000", "country": "Canada"},

    "SPIELBERG":   {"name": "SPIELBERG", "color": "#ED2939", "country": "Austria"},
    "SILVERSTONE": {"name": "SILVERSTONE", "color": "#00247D", "country": "United Kingdom"},
    "SPA":         {"name": "SPA", "color": "#D3020D", "country": "Belgium"},
    "BUDAPEST":    {"name": "BUDAPEST", "color": "#436F4D", "country": "Hungary"},
    "ZANDVOORT":   {"name": "ZANDVOORT", "color": "#21468B", "country": "Netherlands"},

    "MONZA":       {"name": "MONZA", "color": "#CD212A", "country": "Italy"},
    "BAKU":        {"name": "BAKU", "color": "#0098C3", "country": "Azerbaijan"},
    "SINGAPORE":   {"name": "SINGAPORE", "color": "#EF3340", "country": "Singapore"},
    "AUSTIN":      {"name": "AUSTIN", "color": "#B22234", "country": "United States"},
    "MEXICO CITY": {"name": "MEXICO CITY", "color": "#006341", "country": "Mexico"},

    "SAO PAULO":   {"name": "SAO PAULO", "color": "#009C3B", "country": "Brazil"},
    "LAS VEGAS":   {"name": "LAS VEGAS", "color": "#3C3B6E", "country": "United States"},
    "LUSAIL":      {"name": "LUSAIL", "color": "#8A1538", "country": "Qatar"},
    "YAS MARINA":  {"name": "YAS MARINA", "color": "#000000", "country": "United Arab Emirates"},
}

drivers = np.array([(i, F1DriverInfo[i]["color"]) for i in F1DriverInfo.keys()]).reshape(-1, 4, 2)
tracks = np.array([(i, F1TrackInfo[i]["color"]) for i in F1TrackInfo.keys()]).reshape(-1, 4, 2)
# print(tracks)
