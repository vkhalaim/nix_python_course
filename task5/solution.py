def divide_list(list_, n):
    """
    This function divides list to N sublist. N -> len(list) / n.
    If there are no possibility to divide list equally, last item consists of remaining items.
    :param list_: list of elements to divide
    :param n: number of sublists
    :return: list of sublists
    """

    if len(list_) < n or n == 0:
        return list_

    return [list_[i:i + n] for i in range(0, len(list_), n)]
