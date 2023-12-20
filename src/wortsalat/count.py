from wortsalat.preprocess import tokenize_words, split_sentences

def count_total_words(text: str, drop_punctuation=True) -> int:
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

def count_average_word_length(text: str, drop_punctuation=True) -> int:
    """
    Calculate the average length of words in a given text.

    This function tokenizes the input text, calculates the total number of characters in all words, and then divides this total by the number of words to get the average word length.

    Parameters:
    - text (str): The input text for which the average word length will be calculated.

    Returns:
    - float: The average length of words in the input text.
    """
    words = tokenize_words(text, drop_punctuation)
    total_characters = sum(len(word) for word in words)
    length_average_word = total_characters / len(words)
    return length_average_word

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