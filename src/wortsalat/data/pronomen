import nltk
from nltk import word_tokenize, pos_tag

def count_pronouns(text: str) -> int:
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)
    pronoun_count = sum(1 for _, tag in tagged_tokens if tag.startswith("PRP"))
    return pronoun_count

text = "Ich denke wir sollten weiter gehen."

pronouns_count = count_pronouns(text)
print(f"Pronomen: {pronouns_count}")
