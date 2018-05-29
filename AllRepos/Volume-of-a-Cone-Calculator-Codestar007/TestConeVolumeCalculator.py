# TestConeVolumeCalculator.py

# What are we testing for?

# Wide range of inputs
    # - proper and improper
# Boundary Conditions
# Correct outputs
# Test for exceptions

# Import Statements
import unittest
import ConeVolumeCalculator

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription

    def test_calculateConeVolume_for20r10h(self):
        # Capture the results of the function
        result = ConeVolumeCalculator.calculateConeVolume(20.0, 10.0)
        # Check for expected output
        self.assertEqual(4188.79, result)

    def test_calculateConeVolume_for100r10h(self):
        result = ConeVolumeCalculator.calculateConeVolume(100.0, 10.0)
        expected = 104719.76
        self.assertEqual(expected, result)

    # Add minimum of 5 more unittests
    def test_calculateConeVolume_for40r108h(self):
        result = ConeVolumeCalculator.calculateConeVolume(40.0, 108.0)
        expected = 180955.74
        self.assertEqual(expected, result)

    def test_calculateConeVolume_for65_5r80_5h(self):
        result = ConeVolumeCalculator.calculateConeVolume(65.5, 80.5)
        expected = 361665.51
        self.assertEqual(expected, result)

    def test_calculateConeVolume_for65r90h(self):
        result = ConeVolumeCalculator.calculateConeVolume(65, 90)
        expected = 398196.87
        self.assertEqual(expected, result)

    def test_calculateConeVolume_for60r100h(self):
        result = ConeVolumeCalculator.calculateConeVolume(60, 100)
        expected = 376991.12
        self.assertEqual(expected, result)

    def test_calculateConeVolume_for95r80h(self):
        result = ConeVolumeCalculator.calculateConeVolume(95, 80)
        expected = 756076.63
        self.assertEqual(expected, result)

    def test_calculateConeVolume_for100r90h(self):
        result = ConeVolumeCalculator.calculateConeVolume(100, 90)
        expected = 942477.80
        self.assertEqual(expected, result)


# Run the tests
if __name__ == '__main__':
    unittest.main()
