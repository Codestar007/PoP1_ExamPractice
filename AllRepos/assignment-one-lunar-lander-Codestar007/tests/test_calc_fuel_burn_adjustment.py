# test_calc_fuel_burn_adjustment.py
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
                                (12.00, 3.7, 3.7),
                                (1.5, 3.0, 1.5),
                                (0.00, 0.00, 0.00),
                                (3.00, 0.00, 0.00),
                                (10.00, 10.00, 10.00)
                            ]
                            )

def test_calc_fuel_burn_adjustment(fuel_burn, fuel_bal, expected_output):
    result = LunarLander.calc_fuel_burn_adjustment(fuel_burn, fuel_bal)
    assert result == expected_output
    #assert abs(result-expected_output) < 0.0000000001

