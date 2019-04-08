import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc1 = Location("here", 23.4, 23.5)
        self.assertEqual(repr(loc1), "Location('here', 23.4, 23.5)") 
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1 == loc2, False)
        self.assertEqual(loc == loc2, True) 
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
