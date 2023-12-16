from HanTa import HanoverTagger as ht
from numpy import logaddexp
import nltk

tagger = ht.HanoverTagger('morphmodel_ger.pgz')

def count_tags(sentence, taglevel=0):
    words = nltk.word_tokenize(sentence)
    tags = tagger.tag_sent(words, taglevel=taglevel)
    return tags

sentence_1 = "Fachmärkte sind interessant."

tags_1 = count_tags(sentence_1, taglevel=0)

print("POS-tags for Sentence 1:", tags_1)