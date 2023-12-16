***DISCLAIMER: STILL UNDER CONSTRUCTION***

# German NLP Library

## Overview

This Python NLP library is designed specifically for the German language, with a primary focus on analyzing written texts based on a predefined set of secondary language attributes. The library is built upon the insights derived from a scientific paper, outlining a systematic approach to text analysis. The workflow consists of five key steps: Input, Preparation, Identification of search terms, Counting search terms, and Output.

## Installation

To use this library, you can install it via pip:

```bash
pip install german-nlp-library

```

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

## License - The MIT License

Copyright 2023 Petra Barti

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
