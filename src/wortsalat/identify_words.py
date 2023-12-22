def identify_words(key:str, text: str) -> list[str]:
    """
    Identify words in a given text that match a specific word list.

    Parameters:
    - key (str): The word list to match.
    - text (str): The input text for which the words will be identified.

    Returns:
    - list: The words in the input text that match the specified word list.
    """
    word_lists = {
        "ich":  ['ich', 'Ich'],
        "wir":  ['wir', 'Wir'],
        "emojis":   [':)', ':D', '-.-', ':(']
    }
    identified_words = [word for word in text.split() if word in word_lists[key]]

    return identified_words

def count_identified_words(identified_words: list[str]) -> int:
    """
    Count the number of words in a given list.

    Parameters:
    - words (list): The list of words.

    Returns:
    - int: The number of words in the list.
    """
    return len(identified_words)