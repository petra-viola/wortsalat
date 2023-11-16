def count_negative_formulations(text: str) -> int:
    negative_words = ['nicht', 'kein', 'nie', 'niemand', 'nirgendwo', 'nirgends', 'ohne', 'kaum', 'selten']
    negative_words_count = sum(1 for word in text.split() if word in negative_words)
    return negative_words_count

text = "Heute wird kein schöner Tag. Niemand sollte das Haus verlassen."

negative_words_count = count_negative_formulations(text)
print(f"Negative Formulierungen: {negative_words_count}")