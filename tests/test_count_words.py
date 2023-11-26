import pytest

from wortsalat.count_words import count_words


@pytest.mark.parametrize(
        "dictionary,text,expected", 
        [("modalverben", "Petra sollte frueher schlafen gehen", 1),
         ("adjektiv", "Roxy ist ein schoener Hund.", 1),
         ("adverbien", "Roxy lauuft schnell", 1),
         ("artikel", "Der Hund schlaeft.", 1),
         ("emojis", "Viel Spass :)", 1),
         ("emotionalewoerter", "Ich liebe meinen Hund.", 1),
         ("fragewoerter", "Wie geht es dir?", 1),
         ("informellewoerter", "Du bist krass.", 1),
         ("intensitaetswoerter", "Roxy ist sehr schnell", 1),
         ("konjunktionen", "Roxy und Stefan gehen spazieren.", 1),
         ("negativausdruecke", "Heute ist schlechtes Wetter", 1),
         ("nomen", "Das Haus ist groß", 1),
         ("praepositionen", "Der Hund steht auf dem Haus.", 1),
         ("pronomen", "Sie heisst Roxy", 1),
         ("vorsichtigewoerter", "Eventuell war das nicht die beste Idee.", 1)

         ])
def test_count_words(dictionary, text, expected):
    count = count_words(dictionary, text)
    print(count)
    assert count == expected

