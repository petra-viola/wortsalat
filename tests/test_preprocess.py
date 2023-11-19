import pytest

from wortsalat.preprocess import tokenize_words, split_sentences

@pytest.mark.parametrize(
        "text,expected", 
        [("Roxy ist ein schöner Hund.", (['Roxy', 'ist', 'ein', 'schöner', 'Hund', '.'], 6))
         ])
def test_tokenize_words(text, expected):
    words, num_words = tokenize_words(text), 
    print(words, num_words)
    assert words, num_words == expected


@pytest.mark.parametrize(
        "text,expected", 
        [("Heute ist ein schöner Tag. Die Lampe ist an. Das Fenster ist zu.", (['Heute ist ein schöner Tag.', 'Die Lampe ist an.', 'Das Fenster ist zu.'], 3))
         ])
def test_split_sentences(text, expected):
    sentences, num_sentences  = split_sentences(text), 
    print(sentences, num_sentences )
    assert sentences, num_sentences  == expected