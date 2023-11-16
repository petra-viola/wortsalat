import spacy

def calculate_personal_pronoun_percentage(text: str) -> float:
    personal_pronouns = ["Ich", "ich", "wir", "uns"]
    personal_pronoun_count = sum(1 for word in text.split() if word in personal_pronouns)
    total_words = len(text.split())
    personal_pronoun_percentage = (personal_pronoun_count / total_words) * 100
    return personal_pronoun_percentage

text = "Ich gehe heute ins Kino. Wir haben viel Spaß zusammen. Wir mögen Filme."

personal_pronoun_percentage = calculate_personal_pronoun_percentage(text)
print(f"Prozentsatz von 'Ich/wir': {personal_pronoun_percentage:.2f}%")
