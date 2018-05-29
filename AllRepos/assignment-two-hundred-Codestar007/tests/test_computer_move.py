"""test_computer_move.py

CREDIT: Adapted from example given by VLADISLAV RYZHIKOV

Test coverage includes the following:
    All functions that return a value.
    Checking for correct algorithims and output
    Aslo checking for error handling
    Test uses a seed of random number generator of N consecutive calls of random.randint(1,6)
"""
# Import Statements
from context import Hundred
import pytest
import sys
import random

def test_computer_move_inputs1randomseed1_15_20(): # Agressive play i.e 5 rolls
    random.seed(1)   # will produce 2,5,1,3,1,...
    assert Hundred.computer_move(15, 20) == 0

def test_computer_move_inputs1randomseed3_15_15(): # Agressive play i.e 5 rolls
    random.seed(3)   # will produce 2,5,5,2,3,...
    assert Hundred.computer_move(15, 15) == 17

def test_computer_move_inputs1randomseed3_45_20(): # Gentle play i.e 2 rolls
    random.seed(3)   # will produce 2,5,5,2,3,....
    assert Hundred.computer_move(45, 20) == 7

def test_computer_move_inputs1randomseed5_15_10(): # Gentle play i.e 2 rolls
    random.seed(5)   # will produce 5,3,6,3,6,...
    assert Hundred.computer_move(15, 10) == 8

def test_computer_move_inputs1randomseed6_60_31(): # Gentle play i.e 2 rolls
    random.seed(6)   # will produce 5,1,4,3,1,....
    assert Hundred.computer_move(60, 31) == 0

def test_computer_move_inputs1randomseed7_0_0(): # Agressive play i.e 5 rolls
    random.seed(7)  # will produce 3,2,4,6,1,.....
    assert Hundred.computer_move(0, 0) == 0

def test_computer_move_inputs1randomseed7_8_0(): # Gentle play i.e 2 rolls
    random.seed(7)  # will produce 3,2,4,6,1,.....
    assert Hundred.computer_move(8, 0) == 5
