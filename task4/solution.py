def to_upper_strings_with_price(strings):
    """
        Return list of the strings with converted
        to upper case string with 'price' word.
        :param strings: list of the strings
        :return: list of the strings with converted
        strings to upper case which have word 'price'
    """

    return [s.upper() if 'price' in s.lower() else s for s in strings]
