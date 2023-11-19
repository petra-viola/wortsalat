import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK data
nltk.download('punkt')

def tokenize_words(text: str) -> tuple[list[str], int]:
    """
    Tokenize the input text into words using NLTK's word_tokenize.

    Parameters:
    - text (str): The input text to be tokenized.

    Returns:
    tuple: A tuple containing:
        - list: A list of words extracted from the input text.
        - int: The total number of words in the input text.

    Example:
    >>> tokenize_words("This is a sample sentence.")
    (['This', 'is', 'a', 'sample', 'sentence', '.'], 6)
    """
    words = word_tokenize(text)
    num_words = len(words)

    return words, num_words

def split_sentences(text: str) -> tuple[list[str], int]:
    """
    Split the input text into sentences using NLTK's sent_tokenize.

    Parameters:
    - text (str): The input text to be split into sentences.

    Returns:
    tuple: A tuple containing:
        - list: A list of sentences extracted from the input text.
        - int: The total number of sentences in the input text.

    Example:
    >>> split_sentences("This is a sample sentence. Another one follows.")
    (['This is a sample sentence.', 'Another one follows.'], 2)
    """
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)

    return sentences, num_sentences