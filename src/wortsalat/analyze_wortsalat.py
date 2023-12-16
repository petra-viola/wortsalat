import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from HanTa import HanoverTagger as ht
from wortsalat.preprocess import tokenize_words, split_sentences

nltk.download('punkt')

tagger = ht.HanoverTagger('morphmodel_ger.pgz')

def analyze_text(text: str) -> dict:
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    tags = tagger.tag_sent(words, taglevel=0)
    word_lists = {word: [] for word in words}
    for word in words:
        word_lists[word].append(word)
    tag_lists = {tag: [] for word, tag in tags}
    for word, tag in tags:
        tag_lists[tag].append(word)
    num_words = len(words)
    num_sentences = len(sentences)
    total_characters = sum(len(word) for word in words)
    average_word_length = total_characters / num_words
    total_words = sum(len(words) for word, words in word_lists.items())
    average_words_per_sentence = total_words / num_sentences

    analysis = {
        "Words": words,
        "Sentences": sentences,
        "POS-tags": tag_lists,
        "Word_lists": word_lists,
        "Num_words": num_words,
        "Num_sentences": num_sentences,
        "Average_word_length": average_word_length,
        "Average_words_per_sentence": average_words_per_sentence
    }
    return analysis
