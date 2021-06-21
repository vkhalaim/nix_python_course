import unittest

from .solution import filter_list, filter_list_with_unique_values


class TestFilterList(unittest.TestCase):

    def test_nothing_filtered(self):
        self.assertEqual(filter_list([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(filter_list([1, 2, 3, 4], []), [1, 2, 3, 4])
        self.assertEqual(filter_list([1, 2, 3, 4], [5, 6, 7, 8]), [1, 2, 3, 4])

    def test_filtered(self):
        self.assertEqual(filter_list([1, 2, 3, 4], [1, 2]), [3, 4])
        self.assertEqual(filter_list([2, 5, 6, 8], [1, 5, 6]), [2, 8])

    def test_nothing_filtered_unique(self):
        self.assertCountEqual(filter_list_with_unique_values([1, 2, 3], []), [1, 2, 3])
        self.assertCountEqual(filter_list_with_unique_values([1, 2, 3, 4], []), [1, 2, 3, 4])
        self.assertCountEqual(filter_list_with_unique_values([1, 2, 3, 4], [5, 6, 7, 8]), [1, 2, 3, 4])

    def test_filtered_unique(self):
        self.assertCountEqual(filter_list_with_unique_values([1, 2, 3, 4], [1, 2]), [3, 4])
        self.assertCountEqual(filter_list_with_unique_values([2, 5, 6, 8], [1, 5, 6]), [2, 8])


if __name__ == "__main__":
    unittest.main()
