
# sum of numbers
import numpy as np
def addition(a,b):
    return a+b


print(addition(2,3))  # Expected output: 
# sum of numbers
def addition(a, b):
    """Return the sum of a and b."""
    return a + b

import unittest

class TestAddition(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)

if __name__ == "__main__":
    # Run the tests
    unittest.main()













