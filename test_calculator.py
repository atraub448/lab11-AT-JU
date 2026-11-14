# https://github.com/atraub448/lab11-AT-JU
# Partner 1: Aaron Traub
# Partner 2: Jacob Urbina

import unittest
import math
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(4, 12), 16)
        self.assertIs(calculator.add(2, -1), 1)
        self.assertTrue(calculator.add(-5,-15)==-20)
    #     fill in code

    def test_subtract(self): # 3 assertions
        self.assertTrue(calculator.subtract(25,4)==21)
        self.assertIs(calculator.subtract(10, -5), 15)
        self.assertEqual(calculator.subtract(-2,-6),4)
    #     fill in code
    # ##########################

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-3, 4), -12)
        self.assertEqual(calculator.mul(0, 100), 0)

    def test_divide(self):
        # div(a, b) returns b / a
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertAlmostEqual(calculator.div(3, 1), 1 / 3)
        self.assertEqual(calculator.div(-2, 10), -5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -8)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(calculator.logarithm(2, 32), 5)
        self.assertAlmostEqual(calculator.logarithm(3, 81), 4.0)
        self.assertEqual(calculator.logarithm(3, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(-5, 1)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(1, 1), math.sqrt(2))

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(9), 3)
        self.assertEqual(calculator.square_root(0), 0)
        self.assertAlmostEqual(calculator.square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            calculator.square_root(-1)

if __name__ == "__main__":
    unittest.main()