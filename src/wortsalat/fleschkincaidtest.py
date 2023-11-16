import spacy

def syllables_in_word(word):
    # Hier implementieren Sie Ihre Logik zur Ermittlung der Silbenanzahl für ein Wort
    # Das ist nur ein Beispiel und muss möglicherweise angepasst werden.
    # Ein externes Wörterbuch oder eine Bibliothek wie Pyphen kann hier hilfreich sein.
    return 1

def flesch_kincaid_lesbarkeitstest(text):
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(text)

    stopwoerter = nlp.Defaults.stop_words

    wortanzahl = 0
    silbenanzahl = 0
    satzanzahl = 0

    for token in doc:
        if token.is_alpha:
            wortanzahl += 1
            silbenanzahl += syllables_in_word(token.text)

        if token.text in ".!?":
            satzanzahl += 1

    durchschnittliche_wortsilben = silbenanzahl / wortanzahl
    durchschnittliche_wortlaenge = wortanzahl / satzanzahl

    fk_lesbarkeit = 206.835 - (1.015 * durchschnittliche_wortlaenge) - (84.6 * durchschnittliche_wortsilben)

    return {
        "Wortanzahl": wortanzahl,
        "Satzanzahl": satzanzahl,
        "Durchschnittliche Wortsilben": durchschnittliche_wortsilben,
        "Durchschnittliche Wortlänge": durchschnittliche_wortlaenge,
        "Flesch-Kincaid Lesbarkeitstest": fk_lesbarkeit
    }

text = "Dies ist ein Beispieltext in deutscher Sprache. Wir verwenden den Flesch-Kincaid-Lesbarkeitstest, um die Lesbarkeit dieses Textes zu bewerten."

ergebnis = flesch_kincaid_lesbarkeitstest(text)
print(ergebnis)

import textstat

# Sample text for analysis
text = "This is a sample text for readability analysis. It contains multiple sentences and words of varying length."

# Flesch-Kincaid Lesbarkeitstest
flesch_score = textstat.flesch_reading_ease(text)
print(f"Flesch-Kincaid Lesbarkeitstest Score: {flesch_score}")

# Gunning-Fog Index
gunning_fog = textstat.gunning_fog(text)
print(f"Gunning-Fog Index: {gunning_fog}")

# SMOG Index (Simple Measure of Gobbledygook)
smog = textstat.smog_index(text)
print(f"SMOG Index: {smog}")

# Wiener Sachtextformel (for the German language)
wiener_sachtextformel = textstat.wiener_sachtextformel(text)
print(f"Wiener Sachtextformel Score: {wiener_sachtextformel}")