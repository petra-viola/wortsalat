# Liste der Modalverben alle Konjugationen einfügen? Wie wird mit Konjugation umgegangen?
# ChatGPT wollte die "Stopwords" Liste verwenden, aber diese beinhaltet mehr als nur Modalverben

def count_modal_verbs(text: str) -> int:
    modal_verbs = ["kann", "muss", "sollte", "darf", "möchte", "soll", "will", "möge", "dürfe", "könnt", "musst", "wollt", "dürfen", "sollen", "können", "müssen", "wollen", "mögen"]
    modal_count = sum(1 for word in text.split() if word in modal_verbs)
    return modal_count

text = "Der Hund kann laufen, und die Katze sollte auch laufen können."

modal_count = count_modal_verbs(text) 
print("Anzahl der Modalverben im Text:", modal_count)