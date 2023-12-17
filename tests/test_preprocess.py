import pytest

from wortsalat.preprocess import tokenize_words, split_sentences

@pytest.mark.parametrize("text, expected_result", [
    ("This is a sample sentence.", ["This", "is", "a", "sample", "sentence", "."]),
    ("Another example here.", ["Another", "example", "here", "."]),
])
def test_tokenize_words(text, expected_result):
    assert tokenize_words(text) == expected_result

@pytest.mark.parametrize("text, expected_result", [
    ("This is a sample sentence. Another one follows.", ["This is a sample sentence.", "Another one follows."]),
    ("A single sentence.", ["A single sentence."]),
])
def test_split_sentences(text, expected_result):
    assert split_sentences(text) == expected_result

