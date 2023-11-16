import spacy
nlp = spacy.load("de_core_news_sm")

def analyze_intensity_words(text):
    doc = nlp(text)

    total_words = len(doc)
    intensity_words_count = 0
    emotional_words_count = 0

    for token in doc:
        if token.text.lower() in ["glücklich", "traurig", "aufgeregt", "schnell", "fröhlich", "sehr", "extrem", "total", "absolut"]:
            intensity_words_count += 1

    if total_words > 0:
        intensity_ratio = intensity_words_count / total_words
    else:
        intensity_ratio = 0.0

    print("Gesamte Anzahl der Wörter:", total_words)
    print("Anzahl der Intensitätswörter:", intensity_words_count)
    print("Verhältnis von Intensitätswörtern zur Gesamtanzahl der Wörter:", intensity_ratio)

text = "Der schnelle, aufgeregte Hund rannte fröhlich durch den Park. Er war sehr glücklich."

analyze_intensity_words(text)

