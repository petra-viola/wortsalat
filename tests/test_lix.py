import pytest

from wortsalat.lix import calculate_lix

@pytest.mark.parametrize(
        "text,expected", 
        [("Roxy ist ein schöner Hund.", 25)
         ])

def test_lix(text, expected):
    lix = calculate_lix(text)
    print(lix)
    assert lix == expected 