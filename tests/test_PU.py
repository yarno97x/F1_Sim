import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model')))

from PU import PU, PU_constructors

def test_PU_in_constructors() :
    assert isinstance(PU(PU_constructors.MERCEDES).constructor, PU_constructors)
    assert isinstance(PU(PU_constructors.REDBULL_FORD).constructor, PU_constructors)

def test_PU_not_in_constructors() :
    with pytest.raises(TypeError) :
        PU()
    with pytest.raises(TypeError) :
        PU("HELLO")
    with pytest.raises(TypeError) :
        PU(2)


