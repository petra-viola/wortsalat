from importlib import resources as impresources
from . import data

def count_words(type: str ,text: str) -> int:
    """
    Count the number of words in the given text that are present in a specified dictionary.

    Parameters:
    - type (str): The type of dictionary to use. It corresponds to a file within the 'data' package.
    - text (str): The input text in which the words will be counted.

    Returns:
    int: The count of words from the input text that are found in the specified dictionary.

    Example:
    >>> count_words('common', 'This is a common example text.')
    3  # Assuming 'common' dictionary contains the words 'This', 'is', and 'a'.
    """
    inp_file = (impresources.files(data) / type)
    with inp_file.open("rt") as f:
        dictionary = f.readlines()
        dictionary = [line.strip("\n") for line in dictionary]
    count = sum(1 for word in text.split() if word in dictionary)
    return count