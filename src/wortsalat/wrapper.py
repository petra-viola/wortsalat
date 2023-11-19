import textstat

# Flesch-Kincaid Lesbarkeitstest
flesch_score = textstat.flesch_reading_ease(text)
# textstat.set_lang(lang)

# Wiener Sachtextformel (for the German language)
wiener_sachtextformel = textstat.wiener_sachtextformel(text)
