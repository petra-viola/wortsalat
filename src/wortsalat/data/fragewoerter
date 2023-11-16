def count_question_words(text: str) -> int:
    question_words = ["wer", "was", "wann", "wo", "wie", "warum"]
    question_words_count = sum(1 for word in text.split() if word in question_words)
    return question_words_count

text = "Wann hast du Geburtstag? Wer hat das Buch geschrieben? Das ist ein interessantes Thema."

question_words_count = count_question_words(text)
print(f"Fragewörter: {question_words_count}")
