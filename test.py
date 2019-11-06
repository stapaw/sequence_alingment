import pytest
from main import *


def test_possible_moves():
    assert possible_moves(0, 0) == []
    assert possible_moves(1, 0) == [UP]
    assert possible_moves(0, 2) == [LEFT]
    assert possible_moves(1, 1) == [LEFT, UP, UP_LEFT]


def test_global():
    s1 = "CAAGAC"
    s2 = "GAAC"
    line, j = calculate_alignment(s1, s2)
    assert line == "*AA--C"
    assert j == 0


def test_global2():
    s1 = "CAAGTAAGTTA"
    s2 = "CAAGACCT"
    line, j = calculate_alignment(s1, s2)
    assert line == "CAAG-A**T--"


def test_local():
    s1 = "CAAGAC"
    s2 = "AGA"
    line, j = calculate_alignment(s1, s2, LOCAL)
    assert line == "AGA"
    assert j == 2
