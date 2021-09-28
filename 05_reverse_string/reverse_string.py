def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    SplitPhrase = list(phrase)
    SplitPhrase.reverse()
    return ''.join(SplitPhrase)