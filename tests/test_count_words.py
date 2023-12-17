import pytest

from wortsalat.count_words import count_words

@pytest.mark.parametrize(
        "dictionary,text,expected", 
         ("emojis", "Viel Spass :)", 1),
         ])
def test_count_words(dictionary, text, expected):
    count = count_words(dictionary, text)
    print(count)
    assert count == expected

