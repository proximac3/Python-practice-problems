def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # split string and join to avoid spaces.
    result = phrase.split()
    answer =  ''.join(result)

    # use pointer traversal and check each letter.
    start_counter = 0
    end_Counter = len(answer) - 1

    while start_counter != end_Counter:
        if answer[start_counter].lower() != answer[end_Counter].lower():
            return False
        else: 
            start_counter += 1
            end_Counter -= 1
    return True

