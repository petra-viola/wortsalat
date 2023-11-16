import nltk
import re

# nltk.download("punkt")

from nltk import sent_tokenize

def count_passive_constructions(text: str) -> int:
    '''Code Documentation
    '''
    sentences = sent_tokenize(text)
    passive_pattern = re.compile(r'\b(?:werden|ist|sind|war|wurde|wurden|worden)\b', re.IGNORECASE)
    passive_count = 0

    for sentence in sentences:
        if passive_pattern.search(sentence):
            passive_count += 1

    return passive_count

text = "Der Ball wurde von Peter geworfen. Das Buch wird von Maria gelesen. Die Katze jagt den Vogel."

passive_count = count_passive_constructions(text)
print(f"Passivkonstruktionen: {passive_count}")
