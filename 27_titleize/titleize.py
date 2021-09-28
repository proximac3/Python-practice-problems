def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    split_phrase = phrase.split(' ')
    result = []

    for item in split_phrase:
        result.append(item.capitalize())
    return ' '.join(result)