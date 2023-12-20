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
- [LIX](https://de.wikipedia.org/wiki/Lix_(Lesbarkeitsindex))## `wortsalat` Library

## Contributing

It takes a village! 

Special thanks to:
- [perplexity](https://www.perplexity.ai/)
- [phind](https://www.phind.com)
- [chatGPT](https://chat.openai.com)

If you find a bug or have a feature request, please open an issue on GitHub. If you want to contribute to the development of Wortsalat, please fork the repository, make your changes, and then open a pull request.

## License

Wortsalat is released under the MIT License.

### Overview

The `wortsalat` library bietet Funktionen zur Analyse von deutschem Text. Es enthält Funktionen für die Tokenisierung, Satzaufteilung, Identifikation von Wortarten (POS-Tags), Identifikation bestimmter Wörter und verschiedene Textmetriken. Die Bibliothek verwendet externe Tools wie NLTK für die Tokenisierung und Satzaufteilung, HanTa für die POS-Tagging und Textstat für Lesbarkeitsmetriken.

### Installation

Um die Bibliothek zu verwenden, müssen Sie die erforderlichen Abhängigkeiten installieren. Führen Sie den folgenden Befehl aus:

```bash
pip install nltk HanTa textstat
```

### Beispiele

#### Tokenisierung von Wörtern und Satzaufteilung

```python
from wortsalat.preprocess import tokenize_words, split_sentences

text = "Dies ist ein Beispieltext. Er enthält mehrere Sätze."

# Tokenisierung von Wörtern
words = tokenize_words(text)
print("Tokenisierte Wörter:", words)

# Aufteilung in Sätze
sentences = split_sentences(text)
print("Aufgeteilte Sätze:", sentences)
```

#### Identifikation von Wörtern mit einem bestimmten POS-Tag

```python
from wortsalat.identify_tags import identify_tags

text = "Der schnelle braune Fuchs springt über den faulen Hund."

# Identifikation von Wörtern mit dem 'ADJ' (Adjektiv) Tag
adjektive = identify_tags('ADJ', text)
print("Adjektive:", adjektive)
```

#### Analyse von Textmetriken

```python
from wortsalat.wrapper import analyze_wortsalat

text = "Dies ist ein Beispieltext. Er enthält mehrere Sätze."

# Analyse von Textmetriken
small_analysis, big_analysis = analyze_wortsalat(text)

print("Kleine Analyse:")
for key, value in small_analysis.items():
    print(key, ":", value)

print("\nGroße Analyse:")
for key, value in big_analysis.items():
    print(key, ":", value)
```

### Funktionen

1. **Tokenisierung und Satzaufteilung:**
   - `tokenize_words(text: str, drop_punctuation: bool = False) -> list[str]`: Tokenisiert den Eingabetext in Wörter, mit der Möglichkeit, Satzzeichen zu entfernen.
   - `split_sentences(text: str) -> list[str]`: Teilt den Eingabetext in Sätze auf.

2. **Identifikation:**
   - `identify_tags(tag: str, text: str, taglevel: int = 0) -> dict`: Identifiziert Wörter mit einem bestimmten POS-Tag.
   - `identify_words(type: str, text: str) -> list[str]`: Identifiziert Wörter in einem Text, die zu einer bestimmten Wortliste gehören.

3. **Textmetriken:**
   - `count_total_words(text: str, drop_punctuation: bool = False) -> int`: Zählt die Gesamtanzahl der Wörter in einem Text.
   - `count_total_sentences(text: str) -> int`: Zählt die Gesamtanzahl der Sätze in einem Text.
   - `count_average_word_length(text: str) -> float`: Berechnet die durchschnittliche Länge der Wörter in einem Text.
   - `count_average_words_per_sentence(text: str) -> float`: Berechnet die durchschnittliche Anzahl der Wörter pro Satz in einem Text.
   - `count_words_with_tag(words_with_tag: list[str]) -> int`: Zählt die Anzahl der Elemente in einer Liste.
   - `count_identified_words(identified_words: list[str]) -> int`: Zählt die Anzahl der Wörter in einer Liste.

4. **Lesbarkeitsbewertungen:**
   - `calculate_flesch_score(text: str) -> int`: Berechnet den Flesch-Lesbarkeitsindex für einen Text.
   - `calculate_wiener_sachtextformel(text: str) -> int`: Berechnet den Wiener Sachtextformel-Index für einen Text.
   - `calculate_lix(text: str) -> float`: Berechnet den LIX-Lesbarkeitsindex für einen Text.

5. **Textanalyse:**
   - `analyze_wortsalat(text: str) -> dict`: Analysiert einen Text und liefert verschiedene Metriken in kleinen und großen Analysen.
   - `print_wortsalat_small(text: str) -> dict`: Gibt die Ergebnisse der kleinen Analyse der `wortsalat`-Bibliothek aus.
   - `print_wortsalat_big(text: str) -> dict`: Gibt die Ergebnisse der großen Analyse der `wortsalat`-Bibliothek aus.

### Hinweis

- Für eine genaue POS-Tagging stellen Sie sicher, dass die HanTa-Modelldatei (`morphmodel_ger.pgz`) verfügbar ist.

### Lizenz

Diese Bibliothek verwendet die Apache 2.0 Lizenz.

### Mitwirkende

- Diese Bibliothek wurde von [Ihrem Namen] entwickelt und steht für Beiträge offen.

Verwenden Sie diese `wortsalat`-Bibliothek, um deutschen Text zu analysieren und verschiedene linguistische und Lesbarkeitsmetriken zu extrahieren!
## Usage

### 1. Input

Provide the text you want to analyze as input to the library.

```python
from german_nlp_library import GermanNLP

text = "Your German text goes here."
german_nlp = GermanNLP(text)
```

### 2. Preparation

Tokenize the text and split it into sentences.

```python
german_nlp.prepare_text()
```

### 3. Identifying Search Terms

Identify specific search terms in the text, such as verbs, adjectives, and nouns.

```python
german_nlp.identify_search_terms()
```

Searcheable terms include:
Percentage of I/We,
I, me,
first person,
Verbs,
Verbs according to word relationship,
Adverbs,
Adverbs by word relationship,
pronouns,
Pronouns by word ratio,
affiliatory humour,
informal words,
words in total,
articles,
Articles by interaction ratio,
nouns,
Nouns by interaction ratio,
Adjectives,
Adjectives by interaction ratio,
Prepositions,
Prepositions by interaction ratio,
Provisional words*, 
Third person (formality),
Manipulation of T and F,
Words per sentence,
Emojis Emotions negative,
Words related to swearing/danger,
Aggressive humour,
References to facts,
Average length of words,
Words related to emotions,
Emojis Emotions positive,
Emojis neutral,
neutral humour

### 4. Counting Search Terms

Count the occurrences of the identified search terms.

```python
german_nlp.count_search_terms()
```

### 5. Output

Retrieve the analyzed results.

```python
results = german_nlp.get_results()
print(results)
```

### Readability Testing

The library includes functions for testing readability, such as Flesch-Kincaid, Wiener Sachtext-Formel, and LIX.

```python
flesch_score = german_nlp.calculate_flesch_kincaid()
wiener_score = german_nlp.calculate_wiener_sachtext_formel()
lix_score = german_nlp.calculate_lix()

print(f"Flesch-Kincaid Score: {flesch_score}")
print(f"Wiener Sachtext-Formel Score: {wiener_score}")
print(f"LIX Score: {lix_score}")
```

### Testing

The library incorporates testing functionalities to monitor its progress during development. This ensures the robustness and accuracy of the library over time.

```python
german_nlp.run_tests()
```

## Future Development

Continued testing and refinement of the library will be crucial for long-term effectiveness. Additionally, user feedback is highly encouraged to enhance the library's capabilities and address specific needs.

### To Dos

- code examples
- new wordlists
- find new name
- github actions that push te library to pip

## Contributors

- [petra-viola]
- [Other Contributor Names]
