"""test_Hundred.py

Test coverage includes the following:
    All functions that return a value.
    Checking for correct algorithims and output
    Aslo checking for error handling

    Functions tested:
     - is_game_over
     - compare_scores
     - roll
     - ask_yes_or_no


"""

# Import Statements
from context import Hundred
import pytest
import sys
import random


def test_is_game_over():
    assert Hundred.is_game_over(29, 50) is False
    assert Hundred.is_game_over(100, 100) is False
    assert Hundred.is_game_over(120, 120) is False
    assert Hundred.is_game_over(123, 99) is True
    assert Hundred.is_game_over(87, 100) is True

def test_compare_scores():
    assert Hundred.compare_scores(100, 100) == "You are level with the Computer at 100"
    assert Hundred.compare_scores(0, 0) == "You are level with the Computer at 0"
    assert Hundred.compare_scores(76, 25) == "You are 51 BEHIND the Computer"
    assert Hundred.compare_scores(43, 68) == "You are 25 AHEAD of the Computer"

def test_roll_seed_1(): 
    random.seed(1)   # will produce 2,5,1,...
    assert Hundred.roll() == 2

def test_roll_seed_2():
    random.seed(2)   # will produce 1,1,1,...
    assert Hundred.roll() == 1

def test_roll_seed_3():
    random.seed(3)   # will produce 2,5,5,....
    assert Hundred.roll() == 2

def test_roll_seed_5():
    random.seed(5)   # will produce 5,3,6,...
    assert Hundred.roll() == 5

def test_roll_seed_6():
    random.seed(6)   # will produce 5,1,4,....
    assert Hundred.roll() == 5

def test_roll_seed_7():
    random.seed(7)  # will produce 3,2,4,.....
    assert Hundred.roll() == 3

def test_roll_seed_():
    random.seed(9)  # will produce 4,5,3,.....
    assert Hundred.roll() == 4

def test_ask_yes_or_no_NO():
    sys.stdin = open("human_inputs5.txt")  #read input from file. only 1 "N"
    assert Hundred.ask_yes_or_no("Roll dice again? 'Y' or 'N':") == False

def test_ask_yes_or_no_YES():
    sys.stdin = open("human_inputs6.txt")  #read input from file. only 1 "Y"
    assert Hundred.ask_yes_or_no("Roll dice again? 'Y' or 'N':") == True