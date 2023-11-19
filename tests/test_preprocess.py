import pytest

from wortsalat.preprocess import tokenize_words, split_sentences

@pytest.mark.parametrize(
        "text,expected", 
        [("Roxy ist ein schöner Hund.", 25)
         ])

def test_preprocess(text, expected):
    lix = calculate_lix(text)
    print(lix)
    assert lix == expected  