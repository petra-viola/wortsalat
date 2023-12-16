from importlib import resources as impresources
from . import data

def identify_words(type: str, text: str) -> dict:
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
