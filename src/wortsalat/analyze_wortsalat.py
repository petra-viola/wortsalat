import nltk
from HanTa import HanoverTagger as ht

from wortsalat.preprocess import tokenize_words, split_sentences
from wortsalat.count import count_total_words, count_total_sentences, count_average_word_length, count_average_words_per_sentence
#from wortsalat.count import count_tags, count_words
from wortsalat.identify_tags import identify_tags
from wortsalat.identify_words import identify_words
from wortsalat.lix import calculate_lix
from wortsalat.wrapper import calculate_flesch_score, calculate_wiener_sachtextformel
# investigate

nltk.download('punkt')
tagger = ht.HanoverTagger('morphmodel_ger.pgz')

def analyze_text(text: str) -> dict:
    """
    Analyze a given text and return a dictionary with various linguistic statistics.

    This function preprocesses the input text by tokenizing it into words and sentences, and then calculates various linguistic statistics, such as the total number of words and sentences, the average word length and words per sentence, and the number of words that match specific POS tags.

    Parameters:
    - text (str): The input text to analyze.

    Returns:
    - dict: A dictionary with various linguistic statistics.
    """

    #preprocess
    words = tokenize_words(text)
    sentences = split_sentences(text)
    #count
    num_total_words = count_total_words(text)
    num_total_sentences = count_total_sentences(text)
    length_average_word = count_average_word_length(text)
    length_average_sentence = count_average_words_per_sentence(text)
    #num_tags = count_tags(tag_lists)
    #num_words = count_words(word_lists)

    #identify_tags(tag, text, level)
    adjektive = identify_tags(ADJ, words, 0)
    adverbien = identify_tags(ADV, words, 0)
    artikel = identify_tags(ART, words, 0)
    modalverben = identify_tags(VM, words, 0)
    nomen = identify_tags(NN, words, 0)
    praepositionen = identify_words(APPO, APPR, APPRART, APPZR, words, 0)
    pronomen = identify_words(PPER, words, 0)
    verben = identify_words(VA(FIN), VA(IMP), VA(INF), VM(FIN), VM(INF), VM(PP), VV(FIN), VV(IMP), VV(INF), VV(IZU), VV(PP), words, 0)
    
    # ich/ wir
    ich = identify_words(ich, words)
    wir = identify_words(wir, words)
    # emojis = identify_words(emojis, words)

    # Anzahl pro kategorie und verhältnis zur gesamtwortzahl

    lix = calculate_lix(text)
    flesch_kincaid = calculate_flesch_score(text)
    wiener_sachtextformel = calculate_wiener_sachtextformel(text)

    analysis = {
        "words": words,
        "sentences": sentences,
        "total number of words": num_total_words,
        "total number of sentences": num_total_sentences,
        "average words per sentence": length_average_sentence,
        "average word length": length_average_word,
        # "identified pos-tags": num_tags,
        # "identified words": num_words,
        "adjectives": adjektive,
        "adverbs": adverbien,
        "articles": artikel,
        # "share of I/We": ich, wir, 
        "modal verbs": modalverben,
        "nouns": nomen,
        "prepositions": praepositionen,
        "pronouns": pronomen,
        "verbs": verben,
        # "emojis negative":
        # "emojis positive":
        # "emojis neutral":
        "lix": lix,
        "flesch-kincaid": flesch_kincaid,
        "wiener-sachtextformel": wiener_sachtextformel
    }
    return analysis

def print_wortsalat(text: str) -> dict:
    """
    Analyze a given text and print the resulting linguistic statistics.

    This function preprocesses the input text by tokenizing it into words and sentences, and then calculates various linguistic statistics, such as the total number of words and sentences, the average word length and words per sentence, and the number of words that match specific POS tags. It then prints these statistics.

    Parameters:
    - text (str): The input text to analyze.

    Returns:
    - dict: A dictionary with various linguistic statistics.
    """
    text = input()
    analysis = analyze_text(text)
    for key, value in analysis.items():
        print(key, ":", value)