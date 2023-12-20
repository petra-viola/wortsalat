import pytest
from typing import Dict, List
from HanTa import HanoverTagger as ht
from wortsalat.preprocess import tokenize_words, split_sentences
from wortsalat.count import count_total_words, count_total_sentences, count_average_word_length, count_average_words_per_sentence
from wortsalat.identify_words import count_identified_words
from wortsalat.identify_tags import count_words_with_tag

def test_count_total_words():
    text = "Das ist ein interessanter Artikel."
    assert count_total_words(text) == 5

def test_count_total_sentences():
    text = "Das ist ein interessanter Artikel."
    assert count_total_sentences(text) == 1

def test_count_average_word_length():
    text = "Das ist ein interessanter Artikel."
    assert count_average_word_length(text) == 5.8

def test_count_average_words_per_sentence():
    text = "Das ist ein interessanter Artikel."
    assert count_average_words_per_sentence(text) == 5

def test_count_words_with_tag():
    words_with_tag = ['Der', 'Hund', 'Barkt']
    assert count_words_with_tag(words_with_tag) == 3

def test_count_identified_words():
    identified_words = ['Der', 'Hund', 'Barkt']
    assert count_identified_words(identified_words) == 3

