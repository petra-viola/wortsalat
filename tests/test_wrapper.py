import pytest
from wortsalat.wrapper import calculate_wiener_sachtextformel, calculate_flesch_score

# TODO: werte unabhängig prüfen, test funktioniert
@pytest.mark.parametrize("text, expected_score", [
    ("Das hier ist ein Beispielsatz. Hier kommt der nächste.", 83.83), #98
    ("Ein einzelner Satz.", 93.81), #80
    ("Ein komplexer und längerer Satz, mit Wörtern, die über sechs Buchstaben haben.", 76.22), #66
])
def test_calculate_flesch_score(text, expected_score):
    assert calculate_flesch_score(text) == expected_score

# TODO: werte unabhängig prüfen, test funktioniert
@pytest.mark.parametrize("text, expected_score", [
    ("Das hier ist ein Beispielsatz. Hier kommt der nächste.", 60.0),
    ("Ein einzelner Satz.", 80.0),
    ("Ein komplexer und längerer Satz, mit Wörtern, die über sechs Buchstaben haben.", 40.0),
])
def test_calculate_wiener_sachtextformel(text, expected_score):
    assert calculate_wiener_sachtextformel(text) == expected_score
