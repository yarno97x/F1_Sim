import numpy as np
from numpy.linalg import norm 

class Circuit :
    def __init__(self, track = []):
        if type(track) != list or len(track) < 1 :
            raise ValueError("No track given")
        for part in track :
            if type(part) != list or len(part) != 3 :
                raise ValueError("Invalid Track Part")
            for point in part :
                if type(point) != np.ndarray or point.shape != (2,) :
                    raise TypeError("Points should be 2D Numpy arrays")
        if norm(track[0][0] - track[-1][-1]) > 0.1 :
            raise ValueError("Track is not closed")
        
        self.track = [TrackPart(*i) for i in track]

class TrackPart :
    def __init__(self, entry = None, apex = None, end = None) :
        if not all([(type(x) == np.ndarray and x.shape == (2,)) for x in [entry, apex, end]]) :
            raise TypeError("Points should be 2D Numpy arrays")
        elif norm(entry - apex) < 0.01 or norm(entry - end) < 0.01 or norm(apex - end) < 0.01:
            raise ValueError("This is a straight line")

        self.A = entry
        self.B = apex
        self.C = end
        self.angle = self.get_angle()
    
    def get_angle(self) :
        BA = self.B - self.A
        BC = self.B - self.C
        return round(np.acos((np.dot(BA, BC))/(norm(BA) * norm(BC))) * 360 / np.pi / 2, 0) % 180

        
