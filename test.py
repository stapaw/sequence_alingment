import pytest
from main import *

def test_possible_moves():
    assert possible_moves(0, 0) == []
    assert possible_moves(1, 0) == [(-1, 0, UP)]
    assert possible_moves(0, 2) == [(0, -1, LEFT)]
    assert possible_moves(1, 1) == [(0, -1, LEFT), (-1, -1, UP_LEFT), (-1, 0, UP)]
