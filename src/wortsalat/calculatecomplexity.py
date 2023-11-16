import nltk

# nltk.download("punkt")

from nltk import sent_tokenize, word_tokenize

def calculate_complexity_index(text: str) -> float:
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    unique_words = set(words)
    vocab_complexity = len(unique_words) / len(words)
    sentence_complexity = len(sentences) / len(words)
    complexity_index = vocab_complexity + sentence_complexity
    return complexity_index

text = "Einen komplizierten Satz zu schreiben ist einfach. Bei einem langen Text, sieht das jedoch anders aus."

complexity_index = calculate_complexity_index(text)
print(f"Komplexitätsindex: {complexity_index:.2f}")
