def strip_names(string_of_names):
    """
    Return list of names without spaces.
    :param string_of_names: string with names separated with spaces and comas
    :return: list of names (string)
    """
    return [name.strip() for name in string_of_names.split(',')]
