import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')

text = input("Enter the text you want to analyze: ")

def tokenize_words(text: str) -> tuple[list[str]]:
    """
    Tokenize the input text into words using NLTK's word_tokenize.

    Parameters:
    - text (str): The input text to be tokenized.

    Returns:
    tuple: A tuple containing:
        - list: A list of words extracted from the input text.
    """
    words = word_tokenize(text)

    return words

def split_sentences(text: str) -> tuple[list[str]]:
    """
    Split the input text into sentences using NLTK's sent_tokenize.

    Parameters:
    - text (str): The input text to be split into sentences.

    Returns:
    tuple: A tuple containing:
        - list: A list of sentences extracted from the input text.
    """
    sentences = sent_tokenize(text)

    return sentences