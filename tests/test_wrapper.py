import pytest
from wortsalat.wrapper import calculate_wiener_sachtextformel, calculate_flesch_score

# TODO: werte unabhängig prüfen, test funktioniert
@pytest.mark.parametrize("text, expected_score", [
    ("Das hier ist ein Beispielsatz. Hier kommt der nächste.", 83.83),
    ("Ein einzelner Satz.", 93.81),
    ("Ein komplexer und langerer Satz mit Wortern die uber sechs Buchstaben haben.", 76.22),
])
def test_calculate_flesch_score(text, expected_score):
    assert calculate_flesch_score(text) == expected_score

@pytest.mark.parametrize("text, expected_score", [
    ("Das hier ist ein Beispielsatz. Hier kommt der nächste.", 2.4),
    ("Ein einzelner Satz.", 8.2),
    ("Ein komplexer und längerer Satz, mit Wörtern, die über sechs Buchstaben haben.", 8.4),
])
def test_calculate_wiener_sachtextformel(text, expected_score):
    assert calculate_wiener_sachtextformel(text) == expected_score
