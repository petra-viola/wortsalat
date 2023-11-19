import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

def tokenize_words(text):
    words = word_tokenize(text)
    num_words = len(words)

    return words, num_words

def split_sentences(text):
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)

    return sentences, num_sentences 