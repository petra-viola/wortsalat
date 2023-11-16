def calculate_average_sentence_length(text: str) -> float:
    sentences = text.split('.')
    sentence_lengths = [len(sentence.split()) for sentence in sentences]
    average_sentence_length = sum(sentence_lengths) / len(sentence_lengths)
    return average_sentence_length

text = "Das ist ein Text mit ganz vielen Sätzen. So viele. Ein Satz nach dem Anderen. Satz. Satz. Satz."

average_sentence_length = calculate_average_sentence_length(text)
print(f"Satzlänge im Durchschnitt: {average_sentence_length:.2f}")
