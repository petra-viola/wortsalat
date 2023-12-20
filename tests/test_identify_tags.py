import pytest
from wortsalat.identify_tags import identify_tags

def test_identify_tags():
   text = "Dies ist ein Beispieltext. Hier sind einige Adjektive und Verben."
   expected_output = [('ein', 'ein', 'ART')]

   output = identify_tags('ART', text)

   assert output == expected_output
