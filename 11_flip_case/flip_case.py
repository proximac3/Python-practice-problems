def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # split pharse to make it mutable
    split_phrase = list(phrase)
    start_counter = 0;
    
    while start_counter < len(split_phrase) - 1:
        if split_phrase[start_counter] == to_swap:
            split_phrase[start_counter] = split_phrase[start_counter].upper()
        elif split_phrase[start_counter].upper() == to_swap:
            split_phrase[start_counter] = split_phrase[start_counter].lower()
        start_counter += 1 
    return split_phrase
