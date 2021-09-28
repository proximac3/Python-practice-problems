def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
        >>> truncate("Hello World", 6)
        Traceback (most recent call last)
        ...
        ValueError: outside bounds of 1-100
        
    """
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    elif len(phrase) < 3:
        return phrase
    else:
        trimmed_phrase = phrase[0:n - 3]
        return f'{trimmed_phrase}...'
