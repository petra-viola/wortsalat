def count_cautious_words(text: str) -> int:
    cautious_words = ["vielleicht", "eventuell", "möglicherweise", "unter Umständen"]
    cautious_word_count = sum(1 for word in text.split() if word in cautious_words)
    return cautious_word_count

text = "Heute sollten wir unter Umständen einen Regenschirm mitnehmen."
cautious_words_count = count_cautious_words(text)
print(f"Vorsichtige Wörter: {cautious_words_count}")
