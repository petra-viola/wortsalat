def count_informal_words(text: str) -> int:
    informal_words = ["cool", "super", "krass", "geil"]
    informal_word_count = sum(1 for word in text.split() if word in informal_words)
    return informal_word_count

text = "Folgende Wörter sind in Hausarbeiten zu vermeiden: cool, krass, geil, super."

informal_word_count = count_informal_words(text)
print(f"Informelle Wörter: {informal_word_count}")
