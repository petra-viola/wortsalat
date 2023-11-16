import nltk

# nltk.download("punkt")
# nltk.download("averaged_perceptron_tagger")
# nltk.download('universal_tagset')

from nltk import word_tokenize, pos_tag

def count_adverbs(text: str) -> int:
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens, tagset='universal')
    adverb_count = sum(1 for _, tag in tagged_tokens if tag == "ADV")
    return adverb_count

text = "Ich gehe wirklich gerne ins Museum."
adverbs_count = count_adverbs(text)
print(f"Adverbien: {adverbs_count}")
