"""test_human_move.py

CREDIT: Adapted from example given by VLADISLAV RYZHIKOV

Test coverage includes the following:
    All functions that return a value.
    Checking for correct algorithims and output
    Aslo checking for error handling
    Test "Redirects" user input to a file ("human_inputs1(..n).txt") using sys.stdin 
"""
# Import Statements
from context import Hundred
import pytest
import sys
import random

def test_human_move_inputs1randomseed1_15_10():
    sys.stdin = open("human_inputs1.txt")  #read input from file. 3 "Y" and 1 "N"
    random.seed(1)   # will produce 2,5,1,3,1,...
    assert Hundred.human_move(15, 10) == 0

def test_human_move_inputs1randomseed3_15_10():
    sys.stdin = open("human_inputs2.txt")  #read input from file. 8 "Y" and 1 "N"
    random.seed(3)   # will produce 2,5,5,2,3,5,4,6,5,1...
    assert Hundred.human_move(15, 10) == 32

def test_human_move_inputs1randomseed3_5_20():
    sys.stdin = open("human_inputs3.txt")  #read input from file. 11 "Y" and 1 "N"
    random.seed(3)   # will produce 2,5,5,2,3,5,4,6,5,1,5....
    assert Hundred.human_move(5, 20) == 0

def test_human_move_inputs1randomseed5_15_10():
    sys.stdin = open("human_inputs1.txt")  #read input from file. 3 "Y" and 1 "N"
    random.seed(5)   # will produce 5,3,6,3,6,6,6,5,1,...
    assert Hundred.human_move(15, 10) == 14

def test_human_move_inputs1randomseed3_60_31():
    sys.stdin = open("human_inputs4.txt")  #read input from file. 5 "Y" and 1 "N"
    random.seed(3)   # will produce 2,5,5,2,3,5,4,6,5,1,5....
    assert Hundred.human_move(60, 31) == 17

def test_human_move_inputs1randomseed5_0_0():
    sys.stdin = open("human_inputs4.txt")  #read input from file. 5 "Y" and 1 "N"
    random.seed(5)  # will produce 5,3,6,3,6,6,6,5,1,4,2.....
    assert Hundred.human_move(0, 0) == 23

def test_human_move_inputs1randomseed5_23_23():
    sys.stdin = open("human_inputs5.txt")  #read input from file. only 1 "N"
    random.seed(5)  # will produce 5,3,6,3,6,6,6,5,1,4,2.....
    assert Hundred.human_move(23, 23) == 0
