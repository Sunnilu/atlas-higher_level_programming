 #!/usr/bin/python3
'''Unittest for max_integer([..])
'''

import unittest
max_integer = __import__('6-max_integer').max_integer



class TestMaxInteger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1) 
    def test_identical(self):
   
     '''Unittest for max_integer([..])'''
    self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_start(self):
     self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_order(self):
     '''Unittest for max_integer([..])'''
    self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_order_large(self):
    '''Unitest.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) 20)'''
     def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_float_numbers(self):

   def test_identical(self):
    '''Unittest for max_integer([..])'''
    self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_start(self):
    self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_order(self):
    '''Unittest for max_integer([..])'''
    self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_order_large(self):
    '''Unitest.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) 20)'''

if __name__ == '__main__':
    unittest.main() 