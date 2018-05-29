from example2 import *

def test_reverse_string():
    assert reverse_string('foobar!') == '!raboof'
    assert reverse_string('stressed') == 'desserts'

def test_reverse_words():
    assert reverse_words('dogs hate cats') == 'cats hate dogs'
    assert reverse_words('dog eat dog') == 'dog eat dog'
    assert reverse_words('one two three four') == 'four three two one'
