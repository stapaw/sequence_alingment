import pytest
from algorithm import *


def test_possible_moves():
    assert possible_moves(0, 0) == []
    assert possible_moves(1, 0) == [UP]
    assert possible_moves(0, 2) == [LEFT]
    assert possible_moves(1, 1) == [LEFT, UP, UP_LEFT]


def test_global():
    s1 = "CAAGAC"
    s2 = "GAAC"
    line, j , score = calculate_alignment(s1, s2, [1, -1, -2])
    assert line == "*AA--C"
    assert j == 0
    assert score == -2

def test_global2():
    s1 = "CAAGTAAGTTA"
    s2 = "CAAGACCT"
    line, j , score = calculate_alignment(s1, s2, [1, -1, -2])
    assert line == "CAAG-A**T--"
    assert score == -2

def test_global_score():
    s1 = "CAAGAC"
    s2 = "GAAC"
    line, j , score = calculate_alignment(s1, s2, [1, -1, -1])
    assert line == "*AA--C"
    assert j == 0
    assert score == 0



def test_local():
    s1 = "CAAGAC"
    s2 = "AGA"
    line, j , score= calculate_alignment(s1, s2, [1, -1, -2], LOCAL)
    assert line == "AGA"
    assert j == 2
    assert score == 3
