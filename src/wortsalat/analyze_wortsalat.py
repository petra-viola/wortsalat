import nltk
from HanTa import HanoverTagger as ht

from wortsalat.preprocess import tokenize_words, split_sentences
from wortsalat.identify_words import identify_words

nltk.download('punkt')

tagger = ht.HanoverTagger('morphmodel_ger.pgz')

def analyze_text(text: str) -> dict:
    words = tokenize_words(text)
    sentences = split_sentences(text)
    tags = tagger.tag_sent(words, taglevel=0)

    word_lists = {word: [] for word in words}
    for word in words:
        word_lists[word].append(word)

    tag_lists = {tag: [] for tag in tags}
    for word, tag in tags:
        tag_lists[tag].append(word)

    num_words = len(words)
    num_sentences = len(sentences)
    total_characters = sum(len(word) for word in words)
    average_word_length = total_characters / num_words
    total_words = sum(len(words) for word, words in word_lists.items())
    average_words_per_sentence = total_words / num_sentences

    adjektive = identify_words(adjektive, words)
    adverbien = identify_words(adverbien, words)
    artikel = identify_words(artikel, words)
    # emojis = identify_words(emojis, words)
    ich = identify_words(ich, words)
    modalverben = identify_words(modalverben, words)
    nomen = identify_words(nomen, words)
    praepositionen = identify_words(praepositionen, words)
    pronomen = identify_words(pronomen, words)
    verben = identify_words(verben, words)
    verbendritterperson = identify_words(verbendritterperson, words)
    verbenersterperson = identify_words(verbenersterperson, words)
    wir = identify_words(wir, words)

    # ich/ wir

    analysis = {
        "total number of words": num_words,
        "average words per sentence": average_words_per_sentence,
        "average word length": average_word_length,
        # count
        "adjectives": adjektive,
        "adverbs": adverbien,
        "articles": artikel,
        # "share of I/We": ich, wir, 
        "modal verbs": modalverben,
        "nouns": nomen,
        "prepositions": praepositionen,
        "pronouns": pronomen,
        "verbs": verben,
        "third person verbs": verbendritterperson,
        "first person verbs": verbenersterperson,
        # "emojis negative":
        # "emojis positive":
        # "emojis neutral":
        "lix": 
        "flesch-kincaid":
        "wiener-sachtextformel":
    }
    return analysis

def print_wortsalat(text: str) -> dict:
    text = input()
    analysis = analyze_text(text)
    for key, value in analysis.items():
        print(key, ":", value)

#p
def count_total_words(text: str) -> int:
  words = tokenize_words(text)
  num_words = len(words)
  return num_words

def count_total_sentences(text: str) -> int:
  sentences = split_sentences(text)
  num_sentences = len(sentences)
  return num_sentences

def count_average_word_length(text: str) -> float:
  words = tokenize_words(text)
  total_characters = sum(len(word) for word in words)
  lengths_average_word = total_characters / len(words)
  return lengths_average_word

def count_average_words_per_sentence(text: str) -> float:
  sentences = split_sentences(text)
  total_words = sum(len(sentence.split()) for sentence in sentences)
  length_average_sentence = total_words / len(sentences)
  return length_average_sentence

def count_tags(tag_lists: dict) -> dict:
  num_tags = {word: len(words) for word, words in tag_lists.items()}
  return num_tags

def count_words(word_lists: dict) -> dict:
  num_words = {word: len(words) for word, words in word_lists.items()}
  return num_words