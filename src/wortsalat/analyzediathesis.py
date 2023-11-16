import nltk
import re

# nltk.download("punkt")

from nltk import sent_tokenize

def count_active_and_passive_sentences(text: str) -> (int, int):
    sentences = sent_tokenize(text)
    passive_pattern = re.compile(r'\b(?:werden|ist|sind|war|wurde|wurden|worden)\b', re.IGNORECASE)
    active_sentences = 0
    passive_sentences = 0

    for sentence in sentences:
        if passive_pattern.search(sentence):
            passive_sentences += 1
        else:
            active_sentences += 1

    return active_sentences, passive_sentences

text = "Das Fenster wurde geöffnet. Ich öffnete das Fenster."

active_sentences, passive_sentences = count_active_and_passive_sentences(text)
print(f"Aktive Sätze: {active_sentences}, Passive Sätze: {passive_sentences}")
