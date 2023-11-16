def count_emotional_words(text: str) -> int:
    emotional_words = ["glücklich", "traurig", "aufgeregt", "wütend"]
    emotional_words_count = sum(1 for word in text.split() if word in emotional_words)
    return emotional_words_count

text = "Der glückliche Hund sprang aufgeregt herum, während der traurige Hund ängstlich in der Ecke saß."

emotional_words_count = count_emotional_words(text)
print(f"Emotionale Wörter: {emotional_words_count}")