import unittest

from .solution import round_to_hundredth


class TestRoundToHundredthFunction(unittest.TestCase):

    def test_float_to_hundredth(self):
        self.assertAlmostEqual(round_to_hundredth(22.32131), 22.32)
        self.assertAlmostEqual(round_to_hundredth(58.60125), 58.6)
        self.assertAlmostEqual(round_to_hundredth(69.321123), 69.32)
        self.assertAlmostEqual(round_to_hundredth(158.60125), 158.6)

    def test_float_to_int(self):
        self.assertEqual(round_to_hundredth(32.0), 32)
        self.assertEqual(round_to_hundredth(2.0), 2)
        self.assertEqual(round_to_hundredth(0.0), 0)


if __name__ == '__main__':
    unittest.main()
