import unittest

from .solution import to_upper_strings_with_price


class TestToUpperWithPrice(unittest.TestCase):

    def test_without_price(self):
        self.assertEqual(to_upper_strings_with_price(
            ["good job", "well done", "nice"]), ["good job", "well done", "nice"]
        )
        self.assertEqual(to_upper_strings_with_price(
            ["1 job", "well 2", "2"]), ["1 job", "well 2", "2"]
        )

    def test_empty_list(self):
        self.assertEqual(to_upper_strings_with_price([]), [])

    def test_with_price_lower(self):
        self.assertEqual(
            to_upper_strings_with_price(["price", "priceewrewr", "no"]), ["PRICE", "PRICEEWREWR", "no"]
        )
        self.assertEqual(
            to_upper_strings_with_price(["price"]), ["PRICE"]
        )

    def test_with_price_upper(self):
        self.assertEqual(
            to_upper_strings_with_price(["Price is the value of goods"]), ["PRICE IS THE VALUE OF GOODS"]
        )


if __name__ == "__main__":
    unittest.main()
