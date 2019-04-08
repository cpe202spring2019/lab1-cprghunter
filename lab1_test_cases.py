import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Returns the largest integer in a list of integers"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([0, 1, 2, 5, 3, 7]), 7)
        self.assertEqual(max_list_iter([12, 0, 3, 4, 4]), 12)
        self.assertEqual(max_list_iter([]), None)

    def test_reverse_rec(self):
        """Return the list reversed recursively"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([3, 2, 2, 3]), [3, 2, 2, 3])
        self.assertEqual(reverse_rec([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(2, 0, len(list_val) - 1, list_val), 2)
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)
        self.assertEqual(bin_search(8, 0, len(list_val) - 1, list_val), 6)
        self.assertEqual(bin_search(7, 0, len(list_val) - 1, list_val), 5)
        self.assertEqual(bin_search(1, 0, len(list_val) - 1, list_val), 1)
        self.assertEqual(bin_search(0, 0, len(list_val) - 1, list_val), 0)
        self.assertEqual(bin_search(13, 0, len(list_val) - 1, list_val), None)

if __name__ == "__main__":
        unittest.main()

    
