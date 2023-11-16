import spacy

def analyze_first_person_verbs(text):
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(text)

    total_verbs = 0
    first_person_verbs = 0

    for token in doc:
        if token.pos_ == "VERB":
            total_verbs += 1
            if "1" in token.tag_:
                first_person_verbs += 1

    emotional_words = [token.text for token in doc if token.sentiment]
    
    ratio = first_person_verbs / total_verbs if total_verbs > 0 else 0

    print("Alle Wörter im Text:", [token.text for token in doc])
    print("Emotionale Wörter im Text:", emotional_words)
    print("Verhältnis von Verben der ersten Person zu Gesamtverben:", ratio)

text = "Ich gehe heute spazieren, aber gestern bin ich gelaufen. Es regnet, und ich liebe den Regen."

analyze_first_person_verbs(text)