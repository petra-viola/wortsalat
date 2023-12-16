from wortsalat.preprocess import tokenize_words, split_sentences
from wortsalat.identify_tags import tag_lists
from wortsalat.identify_words import word_lists

def count_total_words(text: str) -> int:
    words = tokenize_words(text)
    num_words = len(words)
    return num_words

def count_total_sentences(text: str) -> int:
    sentences = split_sentences(text)
    num_sentences = len(sentences)
    return num_sentences

def count_average_word_length(text: str) -> float:
    words = tokenize_words(text)
    total_characters = sum(len(word) for word in words)
    lenghts_average_word = total_characters / len(words)
    return lenghts_average_word

def count_average_words_per_sentence(text: str) -> float:
    sentences = split_sentences(text)
    total_words = sum(len(sentence.split()) for sentence in sentences)
    length_average_sentence = total_words / len(sentences)
    return length_average_sentence

def count_tags(tag_lists: dict) -> dict:
    num_tags = {word: len(words) for word, words in tag_lists.items()}
    return num_tags

def count_words(word_lists: dict) -> dict:
    num_words = {word: len(words) for word, words in word_lists.items()}
    return num_words


