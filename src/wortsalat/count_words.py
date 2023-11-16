def count_words(input_string):
    """
    Count the number of words in a given string.

    Parameters:
    - input_string (str): The input string to count words from.

    Returns:
    - int: The number of words in the input string.
    """
    # Split the string into a list of words using whitespace as the delimiter
    words = input_string.split()
    
    # Return the count of words
    return len(words)
