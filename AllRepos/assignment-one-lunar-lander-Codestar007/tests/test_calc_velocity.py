# test_calc_velocity.py
# Parametrized unit testing in pytest, adapted from https://www.youtube.com/watch?v=2EGgtlf7BN0

# Test coverage includes the following:
    # All functions that return a value. 
    # Checking for correct algorithims and output
    # Aslo checking for error hnadling

# Import Statements
from context import LunarLander
import pytest


@pytest.mark.parametrize("velocity, fuel_burn, const_s, expected_output",
                            [
                                (12.2499999999999, 3.7, 0.15, 13.2949999999999),
                                (-1.5, 0, 0.15, 0.1),
                                (13.2949999999999, 50, 0.15, 7.3949999999999),
                                (7.39499999999999, 28.54, 0.15, 4.71399999999999),
                                (4.71399999999999, 700, 0.15, -98.686),
                                (-94, 65, 0.15, -102.15)
                            ]
                            )

def test_calc_velocity(velocity, fuel_burn, const_s, expected_output):
    result = LunarLander.calc_velocity(velocity, fuel_burn, const_s)
    #assert result == expected_output
    assert abs(result-expected_output) < 0.0000000001

