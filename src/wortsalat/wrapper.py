import textstat

def calculate_flesch_score(text: str)->int:
    textstat.set_lang("de_DE")
    return textstat.flesch_reading_ease(text)
"""
Calculate the "Flesch reading ease" score of a given text.

This function uses the textstat library to calculate the Flesch reading ease score of a given text.
The Flesch reading ease score is a readability score that indicates how difficult a text is to understand.

Parameters:
- text (str): The text to calculate the Flesch reading ease score for.

Returns:
- float: The Flesch reading ease score of the given text.
"""

def calculate_wiener_sachtextformel(text: str)->int:
    textstat.set_lang("de_DE")
    return textstat.wiener_sachtextformel(text, variant=1)
"""
Calculate the "Wiener Sachtextformel" score of a given text.

This function uses the textstat library to calculate the Wiener Sachtextformel score of a given text.
The Wiener Sachtextformel score is a readability score that indicates how difficult a passage in German is to understand.

Parameters:
- text (str): The text to calculate the Wiener Sachtextformel score for.

Returns:
- float: The Wiener Sachtextformel score of the given text.
"""
