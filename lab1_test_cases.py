import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Returns the largest integer in a list of integers"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        # test that a none list argument raises a ValueError
        with self.assertRaises(ValueError):
            max_list_iter(34)
         #test a max found at end of list
        self.assertEqual(max_list_iter([0, 1, 2, 5, 3, 7]), 7)
         #test a max found at start of list
        self.assertEqual(max_list_iter([12, 0, 3, 4, 4]), 12)
         #test a max found in middle of the list
        self.assertEqual(max_list_iter([0, 1, 3, 12, 4, 4]), 12)
         #test an empty list returns None
        self.assertEqual(max_list_iter([]), None)

    def test_reverse_rec(self):
        """Return the list reversed recursively"""
        # test the raised value error when non list is passed in
        with self.assertRaises(ValueError):
            reverse_rec(34)
         #normal reversed list
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
         #list of size 1 reveresed
        self.assertEqual(reverse_rec([1]), [1])
         #empty list returns empty list
        self.assertEqual(reverse_rec([]), [])
         #test normal reversed list
        self.assertEqual(reverse_rec([3, 2, 2, 3]), [3, 2, 2, 3])
         #test normal reversed list
        self.assertEqual(reverse_rec([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_bin_search(self):
        # test a raised value error when a non list is passed in
        with self.assertRaises(ValueError):
            bin_search("cats are cool", 0, 3, 4)
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
         #find value at first middle split
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
         #find value when high - low is 1
        self.assertEqual(bin_search(2, 0, len(list_val) - 1, list_val), 2)
         #correct index is returned after recursion
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)
         #correct index is returned after recursion 
        self.assertEqual(bin_search(8, 0, len(list_val) - 1, list_val), 6)
         #correct index is returned after recursion
        self.assertEqual(bin_search(7, 0, len(list_val) - 1, list_val), 5)
         #correct index is returned after recursion
        self.assertEqual(bin_search(1, 0, len(list_val) - 1, list_val), 1)
         #correct index is returned after recursion
        self.assertEqual(bin_search(0, 0, len(list_val) - 1, list_val), 0)
         #return none when the value is not found
        self.assertEqual(bin_search(13, 0, len(list_val) - 1, list_val), None)
        #test the high of a 3 item list being the target
        self.assertEqual(bin_search(4, 0, 2, [2, 3, 4]), 2)
        #test the low of a 3 item list being the target
        self.assertEqual(bin_search(2, 0, 2, [2, 3, 4]), 0)

if __name__ == "__main__":
        unittest.main()

    
