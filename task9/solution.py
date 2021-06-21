def filter_list(original_list, values_to_filter):
    """
    Filters original list with values to filter. Order is preserved.
    :param original_list: list of items
    :param values_to_filter: values to filter from original list
    :return: filtered list
    """
    return [elem for elem in original_list if elem not in values_to_filter]


def filter_list_with_unique_values(original_list, values_to_filter):
    """
    Filters original list with values to filter. Order is not preserved.
    :param original_list: list of items
    :param values_to_filter: values to filter from original list
    :return: filtered list
    """
    return list(
        set(original_list) - set(values_to_filter)
    )
