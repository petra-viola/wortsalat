import pytest

from wortsalat.lix import calculate_lix

@pytest.mark.parametrize("text, expected_lix", [
    ("This is a sample sentence. Another one follows.", 20.0),
    ("A single sentence.", 15.0),
    ("A complex and lengthy sentence with words of more than six letters.", 25.0),
])
def test_calculate_lix(text, expected_lix):
    assert calculate_lix(text) == expected_lix
