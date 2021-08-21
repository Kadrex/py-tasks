import pytest
import easy as solution


# find_words()

@pytest.mark.timeout(1.0)
def test__find_words__1():
    test_str = "KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAhven"
    expected = ['Kana', 'Muna', 'Pelmeen', 'Apelsin', 'Õun', 'Mandariin', 'Kakao', 'Hernes', 'Ahven']
    assert solution.find_words(test_str) == expected


@pytest.mark.timeout(1.0)
def test__find_words__2():
    test_str = "Kana!deMuna4fePelmeenApelsinÕun-dawdMandariinKakaoHernes234fe3dAhven"
    expected = ['Kana', 'Muna', 'Pelmeen', 'Apelsin', 'Õun', 'Mandariin', 'Kakao', 'Hernes', 'Ahven']
    assert solution.find_words(test_str) == expected


@pytest.mark.timeout(1.0)
def test__find_words__3():
    test_str = "r324E324fFf0OOOO==ywueRRRe"
    expected = ['Ff', 'Re']
    assert solution.find_words(test_str) == expected


@pytest.mark.timeout(1.0)
def test__find_words__4():
    test_str = "Q324dawUI9!jdjdDD2n"
    expected = []
    assert solution.find_words(test_str) == expected


# find_words_with_vowels()

@pytest.mark.timeout(1.0)
def test__find_words_with_vowels__1():
    test_str = "KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAhven"
    expected = ['Apelsin', 'Õun', 'Ahven']
    assert solution.find_words_with_vowels(test_str) == expected


@pytest.mark.timeout(1.0)
def test__find_words_with_vowels__2():
    test_str = "Kana!deMuna4fePelmeenApelsinÕun-dawdMandariinKakaoHernes234fe3dAhven"
    expected = ['Apelsin', 'Õun', 'Ahven']
    assert solution.find_words_with_vowels(test_str) == expected


@pytest.mark.timeout(1.0)
def test__find_words_with_vowels__3():
    test_str = "r324E324fFf0OOOO==ywueRRReE2GaAAa"
    expected = ['Aa']
    assert solution.find_words_with_vowels(test_str) == expected


@pytest.mark.timeout(1.0)
def test__find_words_with_vowels__4():
    test_str = "A324dawUI9!jdjdED2na"
    expected = []
    assert solution.find_words_with_vowels(test_str) == expected


# find_sentences()

@pytest.mark.timeout(1.0)
def test__find_sentences__1():
    test_str = "See on esimene lause. See on teine lause! see ei ole lause. Aga kas - see - on?jah, oli. See mitte"
    expected = ['See on esimene lause.', 'See on teine lause!', 'Aga kas - see - on?']
    assert solution.find_sentences(test_str) == expected


@pytest.mark.timeout(1.0)
def test__find_sentences__2():
    test_str = "see mitte.Aga see on kohe kindlasti lause.Üks, kaks, kolm! Ja lauses võib ka nime kasutada, näiteks Ago."
    expected = ['Aga see on kohe kindlasti lause.', 'Üks, kaks, kolm!', 'Ja lauses võib ka nime kasutada, näiteks Ago.']
    assert solution.find_sentences(test_str) == expected


@pytest.mark.timeout(1.0)
def test__find_sentences__3():
    test_str = "Ma olen 12-aastane. Kui vana sina oled? Ära valeta, et 15"
    expected = ['Ma olen 12-aastane.', 'Kui vana sina oled?']
    assert solution.find_sentences(test_str) == expected


@pytest.mark.timeout(1.0)
def test__find_sentences__4():
    test_str = "Ma kirjutan vahel ka kolme punktiga lõppevaid lauseid, ei teagi, miks... Või karjun mitme hüüumärgiga!! Või olen nagu: wat????"
    expected = ['Ma kirjutan vahel ka kolme punktiga lõppevaid lauseid, ei teagi, miks...', 'Või karjun mitme hüüumärgiga!!', 'Või olen nagu: wat????']
    assert solution.find_sentences(test_str) == expected


# find_words_from_sentence()

@pytest.mark.timeout(1.0)
def test__find_words_from_sentence__1():
    test_str = "See on esimene lause."
    expected = ['See', 'on', 'esimene', 'lause']
    assert solution.find_words_from_sentence(test_str) == expected
    test_str = "See on teine lause!"
    expected = ['See', 'on', 'teine', 'lause']
    assert solution.find_words_from_sentence(test_str) == expected
    test_str = "Aga kas see on?"
    expected = ['Aga', 'kas', 'see', 'on']
    assert solution.find_words_from_sentence(test_str) == expected


@pytest.mark.timeout(1.0)
def test__find_words_from_sentence__2():
    test_str = ""
    expected = []
    assert solution.find_words_from_sentence(test_str) == expected


@pytest.mark.timeout(1.0)
def test__find_words_from_sentence__3():
    test_str = ""
    expected = []
    assert solution.find_words_from_sentence(test_str) == expected


@pytest.mark.timeout(1.0)
def test__find_words_from_sentence__4():
    test_str = ""
    expected = []
    assert solution.find_words_from_sentence(test_str) == expected

