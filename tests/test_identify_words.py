import pytest
from wortsalat.identify_words import identify_words 

def test_identify_words():
   type = "ich.txt"
   text = "Ich heiße Petra."
   expected_output = ['Ich']

   output = identify_words(type, text)

   assert output == expected_output