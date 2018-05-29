# test_q_has_module_landed.py
# Parametrized unit testing in pytest, adapted from https://www.youtube.com/watch?v=2EGgtlf7BN0

# Test coverage includes the following:
    # All functions that return a value. 
    # Checking for correct algorithims and output
    # Aslo checking for error hnadling

# Import Statements
from context import LunarLander
import pytest


@pytest.mark.parametrize("altitude, velocity, expected_output",
                            [
                                (0.00, 4.25, "Landed"),
                                (-8.00, 7.88, "Landed"),
                                (0.00, 10.00, "Landed"),
                                (0.00, 10.02, "Crashed"),
                                (10.00, 7.35, None),
                                (7.00, -7.35, None)
                            ]
                            )

def test_q_has_module_landed(altitude, velocity, expected_output):
    result = LunarLander.q_has_module_landed(altitude, velocity)
    assert result == expected_output

