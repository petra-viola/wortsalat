import spacy
nlp = spacy.load("de_core_news_sm")

def count_conjunctions(text: str) -> int:
    conjunctions = ["und", "oder", "aber", "denn"]
    conjunction_count = sum(1 for word in text.split() if word in conjunctions)
    return conjunction_count

text = "Ich bin glücklich, dass ich dich sehe, aber es regnet draußen, und deshalb bleibe ich drinnen."

conjunctions_count = count_conjunctions(text)
print(f"Konjunktionen: {conjunctions_count}")

