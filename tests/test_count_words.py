from wortsalat.count_words import count_words

def test_count_words():
    count = count_words("modalverben", "Petra sollte früher schlafen gehen")
    print(count)
    assert count == 1