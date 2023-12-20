from importlib import resources as impresources
from . import data

def identify_words(type: str ,text: str) -> List[str]:
    """
    Identify words in a given text that match a specific word list.

    Parameters:
    - type (str): The word list to match.
    - text (str): The input text for which the words will be identified.

    Returns:
    - list: The words in the input text that match the specified word list.
    """
    inp_file = (impresources.files(data) / type)
    with inp_file.open("rt") as f:
        dictionary = f.readlines()
        dictionary = [line.strip("\n") for line in dictionary]
    identified_words = [word for word in text.split() if word in dictionary]
    return identified_words