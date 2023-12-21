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
from wortsalat.preprocess import tokenize_words

text = "Dies ist ein Beispieltext."
words = tokenize_words(text)
print(words)
```

This will output: `['Dies', 'ist', 'ein', 'Beispieltext', '.']`

### Split Text into Sentences

```python
from wortsalat.preprocess import split_sentences

text = "Dies ist ein Beispieltext. Hier ist eine weitere Satz."
sentences = split_sentences(text)
print(sentences)
```

This will output: `['Dies ist ein Beispieltext.', 'Hier ist eine weitere Satz.']`

### Identify Words That Match a Specific Word List

```python
from wortsalat.identify_words import identify_words

text = "Dies ist ein Beispieltext. Hier ist eine weitere Satz."
words = identify_words(['Dies', 'ist', 'ein'], text)
print(words)
```

This will output: `['Dies', 'ist', 'ein']`

### Identify Words That Match a Specific POS Tag

```python
from wortsalat.identify_tags import identify_tags

text = "Dies ist ein Beispieltext. Hier ist eine weitere Satz."
words = identify_tags('ART', text)
print(words)
```

This will output: `['Dies', 'ein']`

### Count the Total Number of Words

```python
from wortsalat.count import count_total_words

text = "Dies ist ein Beispieltext. Hier ist eine weitere Satz."
num_total_words = count_total_words(text)
print(num_total_words)
```

This will output: `6`

### Calculate the Flesch Reading Ease Score

```python
from wortsalat.wrapper import calculate_flesch_score

text = "Dies ist ein Beispieltext. Hier ist eine weitere Satz."
flesch_score = calculate_flesch_score(text)
print(flesch_score)
```

This will output the Flesch reading ease score of the text.

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
