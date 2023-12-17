from wortsalat.preprocess import tokenize_words, split_sentences
# from wortsalat.identify_tags import tag_lists
# from wortsalat.identify_words import word_lists

def count_total_words(text: str, drop_punctuation=False) -> int:
    """
    Count the total number of words in a given text.

    This function tokenizes the input text and then counts the number of words in the resulting list.

    Parameters:
    - text (str): The input text for which the word count will be calculated.

    Returns:
    - int: The total number of words in the input text.
    """
    words = tokenize_words(text, drop_punctuation)
    num_words = len(words)
    return num_words

def count_total_sentences(text: str) -> int:
    """
    Count the total number of sentences in a given text.

    This function splits the input text into sentences and then counts the number of sentences in the resulting list.

    Parameters:
    - text (str): The input text for which the sentence count will be calculated.

    Returns:
    - int: The total number of sentences in the input text.
    """
    sentences = split_sentences(text)
    num_sentences = len(sentences)
    return num_sentences

def count_average_word_length(text: str) -> float:
    """
    Calculate the average length of words in a given text.

    This function tokenizes the input text, calculates the total number of characters in all words, and then divides this total by the number of words to get the average word length.

    Parameters:
    - text (str): The input text for which the average word length will be calculated.

    Returns:
    - float: The average length of words in the input text.
    """
    words = tokenize_words(text)
    total_characters = sum(len(word) for word in words)
    lenght_average_word = total_characters / len(words)
    return lenght_average_word

def count_average_words_per_sentence(text: str) -> float:
    """
    Calculate the average number of words per sentence in a given text.

    This function splits the input text into sentences, calculates the total number of words in all sentences, and then divides this total by the number of sentences to get the average number of words per sentence.

    Parameters:
    - text (str): The input text for which the average words per sentence will be calculated.

    Returns:
    - float: The average number of words per sentence in the input text.
    """
    sentences = split_sentences(text)
    total_words = sum(len(sentence.split()) for sentence in sentences)
    length_average_sentence = total_words / len(sentences)
    return length_average_sentence

# TODO: funktion fertig schreiben
'''
def count_tags(tag_lists: dict) -> dict:
    """
    Count the number of occurrences of each POS tag in a given dictionary.

    This function takes a dictionary where each key is a POS tag and each value is a list of words assigned that tag, and then counts the number of words assigned each tag.

    Parameters:
    - tag_lists (dict): The dictionary of POS tags and words.

    Returns:
    - dict: A dictionary where each key is a POS tag and each value is the number of words assigned that tag.
    """
    num_tags = {word: len(words) for word, words in tag_lists.items()}
    return num_tags
'''

# TODO: funktion fertig schreiben
'''
def count_words(word_lists: dict) -> dict:
    """
    Count the number of occurrences of each word in a given dictionary.

    This function takes a dictionary where each key is a word and each value is a list of occurrences of that word, and then counts the number of occurrences of each word.

    Parameters:
    - word_lists (dict): The dictionary of words and their occurrences.

    Returns:
    - dict: A dictionary where each key is a word and each value is the number of occurrences of that word.
    """
    num_words = {word: len(words) for word, words in word_lists.items()}
    return num_words
'''
