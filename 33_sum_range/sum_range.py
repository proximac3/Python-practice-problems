def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """

    results = 0

    if start and end:
        counter = start
        new_end = 0
        if end > len(nums):
            new_end = len(nums)
            while counter < new_end:
                results += nums[counter]
                counter += 1
            return results
        else:
            while counter <= end:
                results += nums[counter]
                counter += 1
            return results
    elif start:
        counter = start
        while counter < len(nums):
            results += nums[counter]
            counter += 1
        return results
    elif end:
        counter = 0
        if end > len(nums):
            end = len(nums)
        while counter <= end:
            results += nums[counter]
            counter += 1
        return results
    else:
        counter = 0;
        while counter < len(nums):
            results += nums[counter]
            counter+= 1
        return results

         
nums = [1, 2, 3, 4]