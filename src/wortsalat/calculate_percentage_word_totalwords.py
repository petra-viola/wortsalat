from importlib import resources as impresources
from . import data

def calculate_percentage(type: str, text: str) -> float:
    inp_file = impresources.files(data) / type
    with inp_file.open("rt") as f:
        dictionary = f.readlines()
        dictionary = [line.strip("\n") for line in dictionary]
    
    total_words = len(text.split())
    count = sum(1 for word in text.split() if word in dictionary)
    
    if total_words == 0:
        return 0.0
    
    percentage = (count / total_words) * 100
    return percentage

# Example usage:
text_sample = "This is a sample text. It may contain words that need to be checked."
usage_percentage = calculate_percentage("us", text_sample)
print(f"Usage percentage: {usage_percentage:.2f}%")
