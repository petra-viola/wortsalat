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

    return words_with_tag

