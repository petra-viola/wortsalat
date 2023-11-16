import nltk

# nltk.download("punkt")
# nltk.download("averaged_perceptron_tagger")

from nltk import word_tokenize, pos_tag

def count_adjectives(text: str) -> int:
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens, tagset='universal')
    adjective_count = sum(1 for _, tag in tagged_tokens if tag == "ADJ")
    return adjective_count

text = "Your amazing input text goes here."
adjectives_count = count_adjectives(text)
print(f"Adjektive: {adjectives_count}")
