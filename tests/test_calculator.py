import unittest

import calculator as calc


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertAlmostEqual(calc.add(2.5, 3.2), 5.7)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)
        self.assertEqual(calc.sub(3, 5), -2)

    def test_mul(self):
        self.assertEqual(calc.mul(4, 3), 12)
        self.assertAlmostEqual(calc.mul(2.5, 4), 10.0)

    def test_div(self):
        self.assertEqual(calc.div(10, 2), 5)
        self.assertAlmostEqual(calc.div(7, 2), 3.5)
        with self.assertRaises(ZeroDivisionError):
            calc.div(1, 0)


if __name__ == "__main__":
    unittest.main()
