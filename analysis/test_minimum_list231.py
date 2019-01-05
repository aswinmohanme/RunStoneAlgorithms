import unittest
from minimum_list231 import find_min_n2, find_min

class MinimumNumberTestCase(unittest.TestCase):
    "Test for Finding Minimum Number in List"

    def test_find_min_n2(self):
        "Test if it finds the correct sequence"
        self.assertEqual(find_min_n2([2, 3, 4, 6, 5]), 2)

    def test_find_min(self):
        "Test if It finds the smallest number in least amount"
        self.assertEqual(find_min([2, 3, 4, 6, 5]), 2)

if __name__ == "__main__":
    unittest.main()
