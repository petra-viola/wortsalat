import nltk
from nltk import word_tokenize, pos_tag

def count_articles(text: str) -> int:
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)
    article_count = sum(1 for _, tag in tagged_tokens if tag == "DT")
    return article_count

text= "Der Tisch, das Haus, die Straße."

articles_count = count_articles(text)
print(f"Artikel: {articles_count}")
