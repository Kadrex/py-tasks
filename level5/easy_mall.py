import re


def find_words(text: str) -> list:
    """
    Given string text, return all the words in that string.

    A word here is considered to be any combination letters that starts with
    a capital letter and contains of at least one more lowercase letter.
    Note that Estonian õ, ä, ö and ü should also be accepted here.

    :param text: given string to find words from
    :return: list of words found in given string
    """
    pass


def find_words_with_vowels(text: str) -> list:
    """
    Given string text, return all the words in that string that start with a vowel.

    A word here is considered to be any combination letters that starts with
    a capital letter and contains of at least one more lowercase letter.
    Note that Estonian õ, ä, ö and ü should also be accepted here.

    :param text: given string to find words from
    :return: list of words that start with a vowel found in given string
    """
    pass


def find_sentences(text: str) -> list:
    """
    Given string text, return all sentences in that string.

    A sentence is considered to be
    :param text:
    :return:
    """
    sentences = []
    for match in re.finditer(r"([A-ZÕÄÖÜ][^\.!?]*[\.!?]+)", text):
        sentences.append(match.group(1))
    return sentences


def find_words_from_sentence(sentence: str) -> list:
    return [match.group(1) for match in re.finditer(r"([A-ZÕÄÖÜa-zõäöü\d]+)", sentence)]


def find_words_from_sentences_only(text: str) -> list:
    words = []
    for sentence in find_sentences(text):
        for word in find_words_from_sentence(sentence):
            words.append(word)
    return words


def find_years(text: str) -> list:
    return [int(match.group(1)) for match in re.finditer(r"((?<!\d)\d{4}(?!\d))", text)]


print(find_words('KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAhven'))
print(find_words('Kana!deMuna4fePelmeenApelsinÕun-dawdMandariinKakaoHernes234fe3dAhven'))
print(find_words_with_vowels('KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAhven'))
print(find_sentences('See on esimene - lause. See on ä teine lause! see ei ole lause. Aga kas see on? jah, oli.'))
print(find_sentences('see mitte.Aga see on kohe kindlasti lause.Üks, kaks, kolm! Ja lauses võib ka nime kasutada, näiteks Ago.'))
print(find_sentences('Ma kirjutan vahel ka kolme punktiga lõppevaid lauseid, ei teagi, miks... Või karjun mitme hüüumärgiga!! Või olen nagu: wat????'))
print(find_sentences('Ma olen 12-aastane. Kui vana sina oled? Ära valeta, et 15'))
print(find_words_from_sentences_only('See on esimene - ä lause. See, on teine: lause! see ei ole lause. Aga kas see on? jah, oli.'))
print(find_years("1998sef672387fh3f87fh83777f777f7777f73wfj893w8938434343"))
