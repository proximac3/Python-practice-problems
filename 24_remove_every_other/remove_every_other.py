def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    odd_counter = 0
    results = []

    for number in lst:
        if odd_counter%2 == 0:
            results.append(number)
        odd_counter += 1
    return results
