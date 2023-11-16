def count_third_person_pronouns(text: str) -> int:
    third_person_pronouns = ["er", "sie", "es", "sein", "ihr"]
    third_person_pronoun_count = sum(1 for word in text.split() if word in third_person_pronouns)
    return third_person_pronoun_count

text = "Er ist genauso groß wie sie und ihr Freund."
third_person_pronouns_count = count_third_person_pronouns(text)
print(f"Dritte Person: {third_person_pronouns_count}")
