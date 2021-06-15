def round_to_hundredth(price):
    """
    Return rounded price up to the second decimal
    :param price: float price with several decimals after point
    :return: float price rounded up to the second decimal
    """
    rounded_price = round(price, 2)

    return rounded_price if not rounded_price.is_integer() else int(rounded_price)
