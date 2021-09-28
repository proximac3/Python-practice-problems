def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """
    # if len(ages) < 1:
    #     return 'No ages input'

    ages.sort()
    result_list = []

    counter = len(ages) - 1
    while counter >= 0:
        if ages[counter] in result_list:
            counter -= 1
        else:
            result_list.append(ages[counter])
            counter -= 1
        
        if len(result_list) == 2:
            break
    
    result = set(result_list)

    return tuple(result)


    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.

two_oldest_ages([1, 2, 10, 8])
    