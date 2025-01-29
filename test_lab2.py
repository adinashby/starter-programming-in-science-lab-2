# DO NOT EDIT THIS FILE!! 
# IF MODIFIED IN ANY WAY, YOU WILL RECEIVE 0 FOR THE GRADE!

import unittest
from Lab2 import calculate_height, calculate_car_distance

class TestLab2(unittest.TestCase):
    # Test case for calculate_height() function
    def test_calculate_height(self):
        # Test for different time intervals
        self.assertEqual(calculate_height(50, 1), 45.1)  # 50 - 0.5 * 9.8 * 1^2 = 45.1
        self.assertEqual(calculate_height(50, 2), 30.4)  # 50 - 0.5 * 9.8 * 2^2 = 30.4
        self.assertEqual(calculate_height(50, 3), 5.9)  # 50 - 0.5 * 9.8 * 3^2 = 5.9
        self.assertEqual(calculate_height(50, 0), 50)    # Edge case: at t = 0, height = h0
     
     # Test case for calculate_car_distance() function
    def test_calculate_car_distance(self):
        # Test for different time intervals
        self.assertEqual(calculate_car_distance(1), 20)   # 20 * 1 = 20 meters
        self.assertEqual(calculate_car_distance(2), 40)   # 20 * 2 = 40 meters
        self.assertEqual(calculate_car_distance(3), 60)   # 20 * 3 = 60 meters
    
if __name__ == '__main__':
    unittest.main()
