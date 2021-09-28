def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    value = []
    count = []

    for num in nums:
        if num in value:
            val_index = value.index(num)
            count[val_index] += 1
        else:
            value.append(num)
            count.append(1)
    result = count.index(max(value))
    
    return value[result]