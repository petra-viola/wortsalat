from typing import Dict, List
from HanTa import HanoverTagger as ht
from wortsalat.preprocess import tokenize_words

tagger = ht.HanoverTagger('morphmodel_ger.pgz')

def identify_tags(text: str, taglevel: int = 0) -> Dict[str, List[str]]:
    words = tokenize_words(text)
    tags = tagger.tag_sent(words, taglevel=taglevel)
    tag_lists: Dict[str, List[str]] = {tag: [] for word, tag in tags}
    for word, tag in tags:
        tag_lists[tag].append(word)
    return tag_lists

text = "Fachmärkte sind interessant."

tags = identify_tags(text, taglevel=0)

print("POS-tags:", tags)

'''
    ADJ: adjective
    ADP: adposition
    ADV: adverb
    AUX: auxiliary
    CCONJ: coordinating conjunction
    DET: determiner
    INTJ: interjection
    NOUN: noun
    NUM: numeral
    PART: particle
    PRON: pronoun
    PROPN: proper noun
    PUNCT: punctuation
    SCONJ: subordinating conjunction
    SYM: symbol
    VERB: verb
    X: other
    ????
'''

'''
    ADJ: Adjektiv
    ADP: Adposition
    ADV: Adverb
    AUX: Hilfsgerät
    CCONJ: koordinierende Konjunktion
    DET: Bestimmer
    INTJ: Interjektion
    Substantiv: Substantiv
    NUM: Ziffer
    TEIL: Partikel
    PRON: Pronomen
    PROPN: Eigenname
    PUNCT: Interpunktion
    SCONJ: unterordnende Konjunktion
    SYM: Symbol
    VERB: Verb
    X: andere
'''