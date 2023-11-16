import spacy

def analyse_direkte_anreden(text):
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(text)
    
    wortanzahl = 0
    direkte_anreden = 0
    
    for token in doc:
        if token.is_alpha:
            wortanzahl += 1
            if token.text.lower() in ["du", "sie"]:
                direkte_anreden += 1

    return wortanzahl, direkte_anreden, direkte_anreden / wortanzahl if wortanzahl > 0 else 0

text = "Hallo, wie geht es Ihnen? Guten Tag! Ich hoffe, du hast einen schönen Tag. Bis bald."

wortanzahl, direkte_anreden, verhaeltnis = analyse_direkte_anreden(text)
print(f"Anzahl der Wörter: {wortanzahl}")
print(f"Anzahl der direkten Anreden: {direkte_anreden}")
print(f"Verhältnis direkter Anreden zur Gesamtwortanzahl: {verhaeltnis:.2%}")
