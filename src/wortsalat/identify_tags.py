from typing import Dict, List
from HanTa import HanoverTagger as ht
from wortsalat.preprocess import tokenize_words

tagger = ht.HanoverTagger('morphmodel_ger.pgz')

def identify_tags(text: str, taglevel: int = 0) -> Dict[str, List[str]]:
    """
    Identify POS tags for words in a given text using the Hannover Tagger library.

    This function tokenizes the input text, then uses the Hannover Tagger library to assign POS tags to each word.
    The POS tags are then grouped by tag type, and the function returns a dictionary where each key is a POS tag and the value is a list of words that were assigned that tag.

    Parameters:
    - text (str): The input text for which the POS tags will be identified.
    - taglevel (int): The level of detail of the POS tags to return. Default is 0.

    Returns:
    - Dict[str, List[str]]: A dictionary where each key is a POS tag and each value is a list of words that were assigned that tag.
    """
    words = tokenize_words(text)
    tags = tagger.tag_sent(words, taglevel=taglevel)
    tag_lists: Dict[str, List[str]] = {tag: [] for word, tag in tags}
    for word, tag in tags:
        tag_lists[tag].append(word)
    return tag_lists

text = "Fachmärkte sind interessant."

tags = identify_tags(text, taglevel=0)

print("POS-tags:", tags)