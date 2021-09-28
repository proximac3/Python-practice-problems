def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    frequent = {}

    nums1 = [int(x) for x in str(num1)]
    num2_copy = [int(x) for x in str(num2)]

    for number in nums1:
        if number in num2_copy:
            index_of_num = num2_copy.index(number)
            num2_copy.pop(index_of_num)
        else:
            return False
    return True
    
print(same_frequency(551122, 221515))
    