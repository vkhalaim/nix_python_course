import unittest

from .solution import join_list_with_commas


class TestJoinListWithCommas(unittest.TestCase):

    def test_correct_list(self):
        self.assertEqual(join_list_with_commas(["1", "2", "3"]), "1,2,3")
        self.assertEqual(join_list_with_commas(["V", "K", "J"]), "V,K,J")
        self.assertEqual(join_list_with_commas(["+", "-", "/"]), "+,-,/")
        self.assertEqual(
            join_list_with_commas(["my_string1", "my_string2", "my_string3"]),
            "my_string1,my_string2,my_string3"
        )

    def test_empty_list(self):
        self.assertEqual(join_list_with_commas([]), "")


if __name__ == "__main__":
    unittest.main()
