import unittest

from .solution import strip_names


class TestStripNames(unittest.TestCase):

    def test_ok_input(self):
        self.assertEqual(
            strip_names("Денис, Олег, Вася, Петя,Дима,Женя"),
            ["Денис", "Олег", "Вася", "Петя", "Дима", "Женя"]
        )
        self.assertEqual(
            strip_names("Денис     , Олег, Вася,   Петя,Дима   ,Женя"),
            ["Денис", "Олег", "Вася", "Петя", "Дима", "Женя"]
        )
        self.assertEqual(
            strip_names("Вася,   Петя,Дима   ,Женя"),
            ["Вася", "Петя", "Дима", "Женя"]
        )

    def test_empty_string(self):
        self.assertEqual(strip_names(""), [""])


if __name__ == "__main__":
    unittest.main()
