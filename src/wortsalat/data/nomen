import nltk

# nltk.download("punkt")
# nltk.download("averaged_perceptron_tagger")

from nltk import word_tokenize, pos_tag

def count_nouns(text: str) -> int:
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens, tagset='universal')
    noun_count = sum(1 for _, tag in tagged_tokens if tag in ["NOUN", "PROPN"])
    return noun_count

text = "Your input text goes here."

nouns_count = count_nouns(text)
print(f"Nomen: {nouns_count}")
