from wortsalat.preprocess import tokenize_words, split_sentences
from wortsalat.identify_tags import identify_tags, count_words_with_tag
from wortsalat.identify_words import identify_words, count_identified_words
from wortsalat.count import count_total_words, count_total_sentences, count_average_word_length, count_average_words_per_sentence
from wortsalat.wrapper import calculate_flesch_score, calculate_wiener_sachtextformel
from wortsalat.lix import calculate_lix

def analyze_wortsalat (text: str) -> dict:
    """
    Analyze a given text.
    
    This function tokenizes the input text, splits it into sentences, and then calculates the following metrics:
    - total number of words
    - total number of sentences
    - average word length
    - average words per sentence
    - identified pos-tags
    - identified words
    - number of adjectives
    - number of adverbs
    - number of articles
    - number of modal verbs
    - number of nouns
    - number of prepositions
    - number of pronouns
    - number of verbs
    - number of emojis
    - share of I/We
    - lix
    - flesch-kincaid
    - wiener-sachtextformel
    
    Parameters:
    - text (str): The input text for which the metrics will be calculated.
    
    Returns:
    - dict: A dictionary containing all metrics.

    """
    words = tokenize_words(text)
    sentences = split_sentences(text)

    words_with_tag = identify_tags("ADJA", text)
    identified_words = identify_words("ich.txt", text)

    num_total_words = count_total_words(text)
    num_total_sentences = count_total_sentences(text)
    length_average_word = count_average_word_length(text)
    length_average_sentence = count_average_words_per_sentence(text)
    num_words_with_tag = count_words_with_tag(words_with_tag)
    num_identified_words = count_identified_words(identified_words)

    flesch_kincaid = calculate_flesch_score(text)
    wiener_sachtextformel = calculate_wiener_sachtextformel(text)
    lix = calculate_lix(text)

    adjektive = identify_tags('ADJ', text)
    adverbien = identify_tags('ADV', text)
    artikel = identify_tags('ART', text)
    modalverben = identify_tags('VM', text)
    nomen = identify_tags('NN', text)
    praepositionen = identify_tags('APPO', text)
    pronomen = identify_tags('PPER', text)
    verben = identify_tags("VA", text)
    emojis = identify_words("emojis.txt", text)

    num_adjektive = len(adjektive)
    num_adverbien = len(adverbien)
    num_artikel = len(artikel)
    num_modalverben = len(modalverben)
    num_nomen = len(nomen)
    num_praepositionen = len(praepositionen)
    num_pronomen = len(pronomen)
    num_verben = len(verben)
    num_emojis = len(emojis)

    ratio_adjektive = len(adjektive)/ num_total_words
    ratio_adverbien = len(adverbien)/ num_total_words
    ratio_artikel = len(artikel)/ num_total_words
    ratio_modalverben = len(modalverben)/ num_total_words
    ratio_nomen = len(nomen)/ num_total_words
    ratio_praepositionen = len(praepositionen)/ num_total_words
    ratio_pronomen = len(pronomen)/ num_total_words
    ratio_verben = len(verben)/ num_total_words
    ratio_emojis = len(emojis)/ num_total_words

    ich = identify_words("ich.txt", text)
    wir = identify_words("wir.txt", text)
    ich_wir_verhältnis = len(ich) / len(wir)

    analysis_small = {
        "total number of words": num_total_words,
        "total number of sentences": num_total_sentences,
        "average word length": length_average_word,
        "average words per sentence": length_average_sentence,
        "identified pos-tags": num_words_with_tag,
        "identified words": num_identified_words,
        "number of adjectives": num_adjektive,
        "number of adverbs": num_adverbien,
        "number of articles": num_artikel,
        "number of modal verbs": num_modalverben,
        "number of nouns": num_nomen,
        "number of prepositions": num_praepositionen,
        "number of pronouns": num_pronomen,
        "number of verbs": num_verben,  
        "number of emojis": num_emojis,
        "share of I/We": ich_wir_verhältnis, 
        "lix": lix,
        "flesch-kincaid": flesch_kincaid,
        "wiener-sachtextformel": wiener_sachtextformel
    }

    analysis_big = {
        "total number of words": (num_total_words, words),
        "total number of sentences": (num_total_sentences, sentences),
        "average word length": length_average_word,
        "average words per sentence": length_average_sentence,
        "identified pos-tags": num_words_with_tag,
        "identified words": num_identified_words,
        "adjectives": (num_adjektive, ratio_adjektive, adjektive),
        "adverbs": (num_adverbien, ratio_adverbien, adverbien),
        "articles": (num_artikel, ratio_artikel, artikel),
        "modal verbs": (num_modalverben, ratio_modalverben, modalverben),
        "nouns": (num_nomen, ratio_nomen, nomen),
        "prepositions": (num_praepositionen, ratio_praepositionen, num_praepositionen),
        "pronouns": (num_pronomen, ratio_pronomen, pronomen),
        "verbs": (num_verben, ratio_verben, verben),
        "emojis": (num_emojis, ratio_emojis, emojis),
        "share of I/We": ich_wir_verhältnis, 
        "lix": lix,
        "flesch-kincaid": flesch_kincaid,
        "wiener-sachtextformel": wiener_sachtextformel
    }

    return analysis_small, analysis_big

def print_wortsalat_small(text: str) -> dict:
    """
    Print the results of the small analysis of this 'wortsalat' library.

    Parameters:
    - text (str): The input text for which the metrics will be calculated.

    Returns:
    - dict: A dictionary containing all metrics.
    """
    analysis_small, analysis_big = analyze_wortsalat(text)
    for key, value in analysis_small.items():
        print(key, ":", value)

def print_wortsalat_big(text: str) -> dict:
    """
    Print the results of the big analysis of this 'wortsalat' library.

    Parameters:
    - text (str): The input text for which the metrics will be calculated.

    Returns:
    - dict: A dictionary containing all metrics.
    """
    analysis_big, analysis_small = analyze_wortsalat(text)
    for key, value in analysis_big.items():
        print(key, ":", value)