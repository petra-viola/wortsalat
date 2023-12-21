from wortsalat.analyze_wortsalat import analyze_wortsalat, print_wortsalat_small, print_wortsalat_big 

def test_analyze_words():
    text = "Hallo leute wir sind heute auf einem Bauernhof. Alle Tiere sind in Ordnung nur eins ist doof. Das Rapphuhn. Das rappt nun."
    analyze_wortsalat(text)

def test_print_wortsalat_small():
    text = "Hallo leute wir sind heute auf einem Bauernhof. Alle Tiere sind in Ordnung nur eins ist doof. Das Rapphuhn. Das rappt nun."
    print_wortsalat_small(text)

def test_print_wortsalat_big():
    text = "Hallo leute wir sind heute auf einem Bauernhof. Alle Tiere sind in Ordnung nur eins ist doof. Das Rapphuhn. Das rappt nun."
    print_wortsalat_big(text)