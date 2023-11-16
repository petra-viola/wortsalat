import nltk

# nltk.download("punkt")
# nltk.download("averaged_perceptron_tagger")

from nltk import word_tokenize, pos_tag

def count_prepositions(text: str) -> int:
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens, tagset='universal')
    preposition_count = sum(1 for _, tag in tagged_tokens if tag == "ADP")
    return preposition_count

text = "Your input text goes in here."
prepositions_count = count_prepositions(text)
print(f"Präpositionen: {prepositions_count}")
