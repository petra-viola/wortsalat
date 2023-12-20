from typing import Dict, List
from HanTa import HanoverTagger as ht
from wortsalat.preprocess import tokenize_words

tagger = ht.HanoverTagger('morphmodel_ger.pgz')

def identify_tags(tag: str, text: str, taglevel: int = 0) -> Dict[str, List[str]]:
    """
    This function tags the words using the HanTa library, and then identifies the words that match the specified POS tag.

    https://github.com/wartaal/HanTa

    Parameters:
    - tag (str): The POS tag to match.
    - text (str): The input text for which the POS tags will be identified.
    - taglevel (int): The level of detail of the POS tags to return. Default is 0.

    tags = {
    "adjektive": ["ADJ"],
    "adverbien": ["ADV"],
    "artikel": ["ART"],
    "modalverben": ["VM"],
    "nomen": ["NN"],
    "praepositionen": ["APPO, APPR, APPRART, APPZR"],
    "pronomen": ["PPER"],
    "verben": ["VA(FIN), VA(IMP), VA(INF), VM(FIN), VM(INF), VM(PP), VV(FIN), VV(IMP), VV(INF), VV(IZU), VV(PP)"]
    }

    Returns:
    - Dict[str, List[str]]: A dictionary where each key is a POS tag and each value is a list of words that were assigned that tag.
    """
    words = tokenize_words(text)
    tagged_words = tagger.tag_sent(words, taglevel=1)

    words_with_tag = list()

    for word in tagged_words:
        if word[2] == tag:
            words_with_tag.append(word)

    adjektive = identify_tags('ADJ', words, 0)
    adverbien = identify_tags('ADV', words, 0)
    artikel = identify_tags('ART', words, 0)
    modalverben = identify_tags('VM', words, 0)
    nomen = identify_tags('NN', words, 0)
    #praepositionen = identify_words('APPO', 'APPR', 'APPRART', 'APPZR', words, 0)
    #pronomen = identify_words('PPER', words, 0)
    #verben = identify_words('VA', words, 0)
    
    return words_with_tag, adjektive, adverbien, artikel, modalverben, nomen # praepositionen, pronomen, verben

def count_words_with_tag(words_with_tag: list[str]) -> int:
    """
    Count the number of items in a given list.

    Parameters:
    - words_with_tag (list): The list of words with tags.

    Returns:
    - int: The number of items in the list.
    """
    return len(words_with_tag)