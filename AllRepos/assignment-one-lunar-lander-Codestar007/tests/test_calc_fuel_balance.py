# test_calc_fuel_balance.py
# Parametrized unit testing in pytest, adapted from https://www.youtube.com/watch?v=2EGgtlf7BN0

# Test coverage includes the following:
    # All functions that return a value. 
    # Checking for correct algorithims and output
    # Aslo checking for error hnadling

# Import Statements
from context import LunarLander
import pytest

@pytest.mark.parametrize("fuel_burn, fuel_bal, expected_output",
                            [
                                (67.03, 589, 521.97),
                                (55, 0, 0),
                                (35, 35, 0),
                                (0, 520, 520),
                                (251, 240, 0)
                            ]
                            )

def test_calc_fuel_balance(fuel_burn, fuel_bal, expected_output):
    result = LunarLander.calc_fuel_balance(fuel_burn, fuel_bal)
    #assert result == expected_output
    assert abs(result-expected_output) < 0.0000000001


