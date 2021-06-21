import unittest

from .solution import divide_list


class TestDivideList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(divide_list([], 5), [])

    def test_less_than_n(self):
        self.assertEqual(divide_list([1, 2, 3], 5), [1, 2, 3])
        self.assertEqual(divide_list([1, 2, 3], 54), [1, 2, 3])
        self.assertEqual(divide_list([1, 2], 3), [1, 2])

    def test_multiple_list(self):
        self.assertEqual(divide_list([1, 2, 3], 1), [[1], [2], [3]])
        self.assertEqual(divide_list([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

    def test_remain_list(self):
        self.assertEqual(divide_list([1, 2, 3], 2), [[1, 2], [3]])
        self.assertEqual(divide_list([1, 2, 3, 4, 5], 3), [[1, 2, 3], [4, 5]])


if __name__ == "__main__":
    unittest.main()
