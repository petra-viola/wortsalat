from wortsalat.preprocess import tokenize_words, split_sentences

def calculate_lix(text: str) -> float:
    """
    Calculate the LIX readability index for the given text.

    The LIX index is a measure of text readability, calculated as the sum of the average sentence length
    (number of words per sentence) and the percentage of long words (words with more than six letters).

    Parameters:
    - text (str): The input text for which the LIX index will be calculated.

    Returns:
    float: The LIX readability index for the input text.

    Example:
    >>> calculate_lix("This is a sample text. It contains words of varying lengths.")
    21.43  # Example value; the actual result will depend on the input text.
    """
    words, num_words = tokenize_words(text)

    sentences, num_sentences = split_sentences(text)

    # Zähle die Anzahl der langen Wörter (mehr als sechs Buchstaben)
    long_words = [word for word in words if len(word) > 6]
    num_long_words = len(long_words)
    
    # Berechne den LIX Lesbarkeitsindex
    lix = (num_words / num_sentences) + ((num_long_words * 100) / num_words)
    
    return lix

