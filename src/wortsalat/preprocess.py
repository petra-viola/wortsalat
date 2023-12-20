import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')

punctuation_marks = ["!", "?", "(", ")", ",", ".", "-"]

def tokenize_words(text: str, drop_punctuation=False) -> tuple[list[str]]:
    """
    Tokenize the input text into words using NLTK's word_tokenize.

    https://www.nltk.org/

    Parameters:
    - text (str): The input text to be tokenized.

    Returns:
    tuple: A tuple containing:
    - list: A list of words extracted from the input text.
    """
    words = word_tokenize(text, language="german")
    if drop_punctuation:
        words = [word for word in words if word not in punctuation_marks]

    return words

def split_sentences(text: str) -> tuple[list[str]]:
    """
    Split the input text into sentences using NLTK's sent_tokenize.

    https://www.nltk.org/
    
    Parameters:
    - text (str): The input text to be split into sentences.

    Returns:
    tuple: A tuple containing:
    - list: A list of sentences extracted from the input text.
    """
    sentences = sent_tokenize(text)

    return sentences