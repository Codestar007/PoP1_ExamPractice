def reverse_string(s):
    """
    Reverses order or characters in string s.
    """
    return s #[::-1]

def reverse_words(s):
    """
    Reverses order or words in string s.
    """
    words = s.split()
    words_reversed = words[::-1]
    return ' '.join(words_reversed)

