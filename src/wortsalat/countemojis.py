import spacy

def analyse_emojis(text):
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(text)

    gesuchte_woerter = ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇"]
    alle_woerter = 0
    gesuchte_woerter_vorkommen = 0

    for token in doc:
        alle_woerter += 1
        if token.text in gesuchte_woerter:
            gesuchte_woerter_vorkommen += 1

    verhaeltnis = gesuchte_woerter_vorkommen / alle_woerter

    print(f"Anzahl aller Wörter: {alle_woerter}")
    print(f"Anzahl der Emojis: {gesuchte_woerter_vorkommen}")
    print(f"Verhältnis von Emojis zu allen Wörtern: {verhaeltnis:.2%}")

beispieltext = "Dies ist ein Beispieltext mit Emojis wie 😀, 😃 und 🤣. Schauen wir, wie viele Emojis hier vorkommen."

analyse_emojis(beispieltext)
