# test_calc_altitude.py
# Parametrized unit testing in pytest, adapted from https://www.youtube.com/watch?v=2EGgtlf7BN0

# Test coverage includes the following:
    # All functions that return a value. 
    # Checking for correct algorithims and output
    # Aslo checking for error hnadling

# Import Statements
from context import LunarLander
import pytest


@pytest.mark.parametrize("test_input_1, test_input_2, expected_output",
                            [
                                (991.00, 4.25, 986.75),
                                (788.00, -7.88, 795.88),
                                (0.00, 12.00, -12.00),
                                (0.00, 0.00, 0.00),
                                (10.00, 7.35, 2.65)
                            ]
                            )

def test_calc_altitude(test_input_1, test_input_2, expected_output):
    result = LunarLander.calc_altitude(test_input_1, test_input_2)
    #assert result == expected_output
    assert abs(result-expected_output) < 0.0000000001
