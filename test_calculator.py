# https://github.com/atraub448/lab11-AT-JU
# Partner 1: Aaron Traub
# Partner 2: Jacob Urbina

import unittest
import math
import calculator

class TestCalculator(unittest.TestCase):

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