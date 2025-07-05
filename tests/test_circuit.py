import pytest
import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model')))

from circuit import Circuit, TrackPart
from mock_track import mock_track_parts, mock_track_parts_open

def test_new_trackPart_type_check_error() :
    with pytest.raises(TypeError) :
        TrackPart()
    with pytest.raises(TypeError) :
        TrackPart(1, 2, 3)
    with pytest.raises(TypeError) :
        TrackPart((1, 2), (), {})
    with pytest.raises(TypeError) :
        TrackPart(np.array([1, 2]), [1, 2], np.array([0, 0]))

def test_single_point_error() :
    with pytest.raises(ValueError) :
        TrackPart(np.array([0, 0]), np.array([0, 0]), np.array([0, 0]))
    with pytest.raises(ValueError) :
        TrackPart(np.array([100, 100]), np.array([100, 100]), np.array([100, 100]))

def test_has_track_error() :
    with pytest.raises(ValueError) :
        Circuit()
    with pytest.raises(ValueError) :
        Circuit((0,1))
    with pytest.raises(ValueError) :
        Circuit([])

def test_has_trackparts_error() :
    with pytest.raises(ValueError) :
        Circuit([1, 2, 3])
    with pytest.raises(ValueError) :
        Circuit([np.array([1, 2, 3]), np.array([1, 2, 3]), np.array([1, 2, 3])])
    with pytest.raises(ValueError) :
        Circuit([[np.array([1, 2]), np.array([1, 2])]])

def test_has_points_error() :
    with pytest.raises(TypeError) :
        Circuit([[np.array([1, 2]), np.array([1, 2]), 2]])
    with pytest.raises(TypeError) :
        Circuit([[np.array([1, 2]), np.array([1, 2, 3]), np.array([1, 2])]])

def test_error_open_track() :
    with pytest.raises(ValueError) :
        Circuit(mock_track_parts_open)

def test_working_circuit() :
    assert hasattr(Circuit(mock_track_parts), "track")
