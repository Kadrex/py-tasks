import re


def find_words(text: str) -> list:
    words = []
    for match in re.finditer(r"([A-ZÕÄÖÜ][a-zõäöü]+)", text):
        words.append(match.group())
    return words


def find_words_with_vowels(text: str) -> list:
    words = []
    for match in re.finditer(r"([AEIOUÕÄÖÜ][a-zõäöü]+)", text):
        words.append(match.group())
    return words


def find_sentences(text: str) -> list:
    sentences = []
    for match in re.finditer(r"([A-Z][^\.!?]*[\.!?])", text):
        sentences.append(match.group(1))
    return sentences


def find_words_from_sentence(sentence: str) -> list:
    return [match.group(1) for match in re.finditer(r"([A-ZÕÄÖÜa-zõäöü]+)", sentence)]


def find_words_from_sentences_only(text: str) -> list:
    words = []
    for sentence in find_sentences(text):
        for word in find_words_from_sentence(sentence):
            words.append(word)
    return words


def find_years(text: str) -> list:
    return [match.group(1) for match in re.finditer(r"((?<!\d)\d{4}(?!\d))", text)]


print(find_words('KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAhven'))
print(find_words('Kana!deMuna4fePelmeenApelsinÕun-dawdMandariinKakaoHernes234fe3dAhven'))
print(find_words_with_vowels('KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAhven'))
print(find_sentences('See on esimene - lause. See on ä teine lause! see ei ole lause. Aga kas see on? jah, oli.'))
print(find_words_from_sentences_only('See on esimene - ä lause. See, on teine: lause! see ei ole lause. Aga kas see on? jah, oli.'))
print(find_years("1998sef672387fh3f87fh83777f777f7777f73wfj893w8938434343"))
