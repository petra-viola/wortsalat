from importlib import resources as impresources
from . import data

def identify_words(type: str, text: str) -> dict:
    """
    Identify words in a text that are present in a specific dictionary.

    This function reads a dictionary from a file, and then checks if each word in the provided text is present in the dictionary.
    The dictionary file is expected to be located in the 'data' package, and the type of dictionary is specified by the 'type' parameter.

    Parameters:
    - type (str): The type of dictionary to use. This should correspond to a file in the 'data' package.
    - text (str): The text to check for words present in the dictionary.

    Returns:
    - Dict[str, list]: A dictionary where each key is a word from the text, and the value is a list containing that word if it was found in the dictionary.
    """
    inp_file = (impresources.files(data) / type)
    with inp_file.open("rt") as f:
        dictionary = f.readlines()
        dictionary = [line.strip("\n") for line in dictionary]
    words = text.split()
    word_lists = {word: [] for word in words}
    for word in words:
        if word in dictionary:
            word_lists[word].append(word)
    return word_lists
