from importlib import resources as impresources
from . import data

def calculate_percentage_me_us(type: str ,text: str) -> int:
    inp_file = (impresources.files(data) / type)
    with inp_file.open("rt") as f:
        dictionary = f.readlines()
        dictionary = [line.strip("\n") for line in dictionary]
    count = sum(1 for word in text.split() if word in dictionary)
    return count