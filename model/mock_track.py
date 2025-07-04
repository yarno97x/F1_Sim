import numpy as np

mock_track_parts = [
    [np.array([0.0, 0.0]), np.array([50.0, 0.0]), np.array([100.0, 0.0])],         # Straight
    [np.array([100.0, 0.0]), np.array([120.0, 20.0]), np.array([100.0, 40.0])],    # Right curve
    [np.array([100.0, 40.0]), np.array([50.0, 60.0]), np.array([0.0, 40.0])],      # Top straight
    [np.array([0.0, 40.0]), np.array([-20.0, 20.0]), np.array([0.0, 0.0])],        # Left curve back to start
]

mock_track_parts_open = [
    [np.array([0.0, 0.0]), np.array([50.0, 0.0]), np.array([100.0, 0.0])],         # Straight
    [np.array([100.0, 0.0]), np.array([120.0, 20.0]), np.array([100.0, 40.0])],    # Right curve
    [np.array([100.0, 40.0]), np.array([50.0, 60.0]), np.array([0.0, 40.0])],      # Left curve 
]
