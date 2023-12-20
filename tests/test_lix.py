import pytest

from wortsalat.lix import calculate_lix

@pytest.mark.parametrize("text, expected_lix", [
    ("LIX ist ein Lesbarkeitsindex, der die Schwierigkeit angibt, einen Text lesen zu können. Er wurde von Carl-Hugo Björnsson formuliert.", 36.0),
    ("A single sentence.", 15.0),
    ("A complex and lengthy sentence with words of more than six letters.", 25.0),
])
def test_calculate_lix(text, expected_lix):
    assert pytest.approx(calculate_lix(text), 1) == expected_lix
