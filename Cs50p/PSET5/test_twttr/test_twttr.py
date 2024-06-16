import pytest
import twttr

def test_shorten():
    assert twttr.shorten('Hello') == 'Hll'
    assert twttr.shorten('world') == 'wrld'
    assert twttr.shorten('AEIOU') == ''
    assert twttr.shorten('aeiou') == ''
    assert twttr.shorten('') == ''
def test_shorten_with_punctuation():
    assert twttr.shorten('Hello, world!') == 'Hll, wrld!'
def test_shorten_with_numbers():
    assert twttr.shorten('Hello123') == 'Hll123'
