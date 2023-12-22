# Wortsalat

Wortsalat is a Python library that provides various linguistic analysis tools for text data. It includes functions for tokenizing text into words and sentences, identifying words that match specific word lists or POS tags, counting the total number of words and sentences, calculating the average word length and words per sentence, and calculating various readability scores.

## Installation

You can install Wortsalat from PyPI:

```bash
pip install wortsalat
```

## Usage

Here are some examples of how to use the functions provided by Wortsalat:

### Tokenize Text into Words

```python
from wortsalat import preprocess
from wortsalat.preprocess import tokenize_words

text = "Dies ist ein Beispieltext."
words = tokenize_words(text)
print(words)
```

This will output: `['Dies', 'ist', 'ein', 'Beispieltext', '.']`

### Split Text into Sentences

```python
from wortsalat import preprocess
from wortsalat.preprocess import split_sentences

text = "Dies ist ein Beispieltext. Hier ist eine weitere Satz."
sentences = split_sentences(text)
print(sentences)
```

This will output: `['Dies ist ein Beispieltext.', 'Hier ist eine weitere Satz.']`

### Identify Words That Match a Specific Word List

```python
from wortsalat import identify_words
from wortsalat.identify_words import identify_words

text = "Dies ist ein Beispieltext. Hier ist eine weitere Satz."
words = identify_words('ich', text)
print(words)
```

This will output: `[]`

### Identify Words That Match a Specific POS Tag

```python
from wortsalat import identify_tags
from wortsalat.identify_tags import identify_tags

text = "Dies ist ein Beispieltext. Hier ist eine weitere Satz."
words = identify_tags('ART', text)
print(words)
```

This will output: `[('eine', 'ein', 'ART')]`

### Count the Total Number of Words

```python
from wortsalat import count
from wortsalat.count import count_total_words

text = "Dies ist ein Beispieltext. Hier ist eine weitere Satz."
num_total_words = count_total_words(text)
print(num_total_words)
```

This will output: `9`

### Analyze Wortsalat

```python
from wortsalat import analyze_wortsalat
from wortsalat.analyze_wortsalat import analyze_wortsalat

text = "Dies ist ein Beispieltext. Hier ist eine weitere Satz."
analysis = analyze_wortsalat(text)
print(analysis)
```

This will output:
```(
    {
        'total number of words': 9,
        'total number of sentences': 2,
        'average word length': 4.888888888888889,
        'average words per sentence': 4.5,
        'identified pos-tags': 0,
        'identified words': 0,
        'number of adjectives': 0,
        'number of adverbs': 1,
        'number of articles': 2,
        'number of modal verbs': 0,
        'number of nouns': 2,
        'number of prepositions': 0,
        'number of pronouns': 0,
        'number of verbs': 0,
        'number of emojis': 0,
        'share of I/We': None,
        'lix': 26.72222222222222,
        'flesch-kincaid': 81.9,
        'wiener-sachtextformel': 4.9
    },
    {
        'total number of words': (
            9,
            [
                'Dies',
                'ist',
                'ein',
                'Beispieltext',
                '.',
                'Hier',
                'ist',
                'eine',
                'weitere',
                'Satz',
                '.'
            ]
        ),
        'total number of sentences': (
            2,
            ['Dies ist ein Beispieltext.', 'Hier ist eine weitere Satz.']
        ),
        'average word length': 4.888888888888889,
        'average words per sentence': 4.5,
        'identified pos-tags': 0,
        'identified words': 0,
        'adjectives': (0, 0.0, []),
        'adverbs': (1, 0.1111111111111111, [('Hier', 'hier', 'ADV')]),
        'articles': (2, 0.2222222222222222, [('ein', 'ein', 'ART'), ('eine', 'ein', 'ART')]),
        'modal verbs': (0, 0.0, []),
        'nouns': (
            2,
            0.2222222222222222,
            [('Beispieltext', 'beispiel+text', 'NN'), ('Satz', 'satz', 'NN')]
        ),
        'prepositions': (0, 0.0, 0),
        'pronouns': (0, 0.0, []),
        'verbs': (0, 0.0, []),
        'emojis': (0, 0.0, []),
        'share of I/We': None,
        'lix': 26.72222222222222,
        'flesch-kincaid': 81.9,
        'wiener-sachtextformel': 4.9
    }
)
```

## References

- [NLTK](https://www.nltk.org/)
- [HanTa](https://github.com/wartaal/HanTa)
- [textstat](https://pypi.org/project/textstat/)

## Contributing - It takes a village!

- [thespaceinvader](https://github.com/thespaceinvader)

If you find a bug or have a feature request, please open an issue on GitHub. If you want to contribute to the development of Wortsalat, please fork the repository, make your changes, and then open a pull request.

Additional thanks to:
- [perplexity](https://www.perplexity.ai/)
- [phind](https://www.phind.com)
- [chatGPT](https://chat.openai.com)

## License

Wortsalat is released under the Apache 2.0 License.
