from wortsalat.preprocess import tokenize_words, sent_tokenize

def calculate_lix(text):
    words, num_words = tokenize_words(text)

    sentences, num_sentences = sent_tokenize(text)

    # Zähle die Anzahl der langen Wörter (mehr als sechs Buchstaben)
    long_words = [word for word in words if len(word) > 6]
    num_long_words = len(long_words)
    
    # Berechne den LIX Lesbarkeitsindex
    lix = (num_words / num_sentences) + ((num_long_words * 100) / num_words)
    
    return lix
 