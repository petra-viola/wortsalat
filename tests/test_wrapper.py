import pytest
import textstat

# Test the calculate_flesch_score function
@pytest.mark.parametrize("text, expected_score", [
    ("This is a sample sentence. Another one follows.", 100.0),
    ("A single sentence.", 100.0),
    ("A complex and lengthy sentence with words of more than six letters.", 70.0),
])
def test_calculate_flesch_score(text, expected_score):
    assert textstat.flesch_reading_ease(text) == expected_score

# Test the calculate_wiener_sachtextformel function
@pytest.mark.parametrize("text, expected_score", [
    ("This is a sample sentence. Another one follows.", 60.0),
    ("A single sentence.", 80.0),
    ("A complex and lengthy sentence with words of more than six letters.", 40.0),
])
def test_calculate_wiener_sachtextformel(text, expected_score):
    assert textstat.wiener_sachtextformel(text) == expected_score
