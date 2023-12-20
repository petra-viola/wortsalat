from wortsalat.preprocess import tokenize_words, split_sentences
from wortsalat.count import count_total_words, count_total_sentences

def calculate_lix(text: str) -> float:
    """
    Calculate the LIX readability index for the given text.

    The LIX index is a measure of text readability, calculated as the sum of the average sentence length
    (number of words per sentence) and the percentage of long words (words with more than six letters).
    This readability measure was developed by Swedish scholar Carl-Hugo Björnsson.

    https://de.wikipedia.org/wiki/Lix_(Lesbarkeitsindex)

    Parameters:
    - text (str): The input text for which the LIX index will be calculated.

    Returns:
    - float: The LIX readability index for the input text.
    """
    words = tokenize_words(text, drop_punctuation=True)
    num_words = count_total_words(text, drop_punctuation=True)

    sentences = split_sentences(text)
    num_sentences = count_total_sentences(text)

    long_words = [word for word in words if len(word) > 6]
    num_long_words = len(long_words)

    print(words, num_words, sentences, num_sentences, long_words, num_long_words)
    
    lix = (num_words / num_sentences) + ((num_long_words * 100) / num_words)
    
    return lix

