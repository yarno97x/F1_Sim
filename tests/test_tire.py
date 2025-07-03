import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tire import *

def test_tire_creation() :
    for kind in [Soft, Medium, Hard, Inter, Wet] :
        x = kind()
        assert (hasattr(x, "life") and hasattr(x, "color"))

def test_tire_colors() :
    colors = {
        Soft : 0xFF4444, 
        Medium : 0xFFD700, 
        Hard : 0xE0E0E0, 
        Inter : 0x33FF33, 
        Wet : 0x3399FF
    }

    for kind, hex in colors.items():
        x = kind()
        assert hasattr(x, "color") and x.color == hex
