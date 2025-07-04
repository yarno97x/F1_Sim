from enum import Enum
import numpy as np

class IndicatorType(Enum) :
    DRS = {"text" : "DRS", "color" : "#00B050"}
    OUT = {"text" : "OUT", "color" : "#4E95D9"}
    PIT = {"text" : "PIT", "color" : "#FF0000"}

class F1Driver(Enum):
    VERSTAPPEN = {"name": "Max Verstappen", "color": "#1E41FF"}       # Red Bull
    TSUNODA = {"name": "Yuki Tsunoda", "color": "#1E41FF"}            # Red Bull

    LECLERC = {"name": "Charles Leclerc", "color": "#DC0000"}         # Ferrari
    HAMILTON = {"name": "Lewis Hamilton", "color": "#DC0000"}         # Ferrari

    RUSSELL = {"name": "George Russell", "color": "#00D2BE"}          # Mercedes
    ANTONELLI = {"name": "Kimi Antonelli", "color": "#00D2BE"}        # Mercedes

    NORRIS = {"name": "Lando Norris", "color": "#FF8700"}             # McLaren
    PIASTRI = {"name": "Oscar Piastri", "color": "#FF8700"}           # McLaren

    ALONSO = {"name": "Fernando Alonso", "color": "#006F62"}          # Aston Martin
    STROLL = {"name": "Lance Stroll", "color": "#006F62"}             # Aston Martin

    LAWSON = {"name": "Liam Lawson", "color": "#6692FF"}              # VCARB
    HADJAR = {"name": "Isack Hadjar", "color": "#6692FF"}             # VCARB

    HULKENBERG = {"name": "Nico Hulkenberg", "color": "#66994D"}      # Kick Sauber
    BORTOLETO = {"name": "Gabriel Bortoleto", "color": "#66994D"}     # Kick Sauber

    OCON = {"name": "Esteban Ocon", "color": "#B6BABD"}               # Haas
    BEARMAN = {"name": "Oliver Bearman", "color": "#B6BABD"}          # Haas

    SAINZ = {"name": "Carlos Sainz", "color": "#005AFF"}              # Williams
    ALBON = {"name": "Alex Albon", "color": "#005AFF"}                # Williams

    GASLY = {"name": "Pierre Gasly", "color": "#0090FF"}              # Alpine (?)
    COLAPINTO = {"name": "Franco Colapinto", "color": "#0090FF"}      # Alpine (?)

class F1Track(Enum):
    MELBOURNE = {"name": "MELBOURNE", "color": "#00008B"}       # Australia
    SHANGHAI = {"name": "SHANGHAI", "color": "#FF0000"}         # China
    SUZUKA = {"name": "SUZUKA", "color": "#BC002D"}             # Japan
    SAKHIR = {"name": "SAKHIR", "color": "#D71A28"}             # Bahrain
    JEDDAH = {"name": "JEDDAH", "color": "#006C35"}             # Saudi Arabia

    MIAMI = {"name": "MIAMI", "color": "#3C3B6E"}               # USA
    IMOLA = {"name": "IMOLA", "color": "#008C45"}               # Italy
    MONACO = {"name": "MONACO", "color": "#ED1C24"}             # Monaco
    BARCELONA = {"name": "BARCELONA", "color": "#AA151B"}       # Spain
    MONTREAL = {"name": "MONTREAL", "color": "#FF0000"}         # Canada

    SPIELBERG = {"name": "SPIELBERG", "color": "#ED2939"}       # Austria
    SILVERSTONE = {"name": "SILVERSTONE", "color": "#00247D"}   # UK
    SPA = {"name": "SPA", "color": "#D3020D"}                   # Belgium (updated for readability)
    BUDAPEST = {"name": "BUDAPEST", "color": "#436F4D"}         # Hungary
    ZANDVOORT = {"name": "ZANDVOORT", "color": "#21468B"}       # Netherlands

    MONZA = {"name": "MONZA", "color": "#CD212A"}               # Italy
    BAKU = {"name": "BAKU", "color": "#0098C3"}                 # Azerbaijan
    SINGAPORE = {"name": "SINGAPORE", "color": "#EF3340"}       # Singapore
    AUSTIN = {"name": "AUSTIN", "color": "#B22234"}             # USA
    MEXICO_CITY = {"name": "MEXICO_CITY", "color": "#006341"}   # Mexico

    SAO_PAULO = {"name": "SAO_PAULO", "color": "#009C3B"}       # Brazil
    LAS_VEGAS = {"name": "LAS_VEGAS", "color": "#3C3B6E"}       # USA
    LUSAIL = {"name": "LUSAIL", "color": "#8A1538"}             # Qatar
    YAS_MARINA = {"name": "YAS_MARINA", "color": "#000000"}     # Abu Dhabi

drivers = np.array(list(F1Driver)).reshape(-1, 4)
tracks = np.array(list(F1Track)).reshape(-1, 4)
