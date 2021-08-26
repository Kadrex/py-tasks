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


def find_phone_numbers(text: str) -> list:
    result = dict()
    for match in re.finditer(r"((\+\d{3}) ?)?(\d{7,8})", text):
        if match.group(2):
            if match.group(2) in result.keys():
                result[match.group(2)].append(match.group(3))
            else:
                result[match.group(2)] = [match.group(3)]
        else:
            if "" in result.keys():
                result[""].append(match.group(3))
            else:
                result[""] = [match.group(3)]
    return result


print(find_words('KanaMunaPelmeen!!ApelsinÕunMandariinKakaoHernesAhven'))  # ['Kana', 'Muna', 'Pelmeen', 'Apelsin', 'Õun', 'Mandariin', 'Kakao', 'Hernes', 'Ahven']
print(find_words_with_vowels('KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAhven'))  # ['Apelsin', 'Õun', 'Ahven']
print(find_sentences('See on esimene - lause. See on ä teine lause! see ei ole lause. Aga kas see on? jah, oli.'))  # ['See on esimene - lause.', 'See on ä teine lause!', 'Aga kas see on?']
print(find_words_from_sentence("Super lause ää, sorry."))  # ['Super', 'lause', 'ää', 'sorry']
print(find_words_from_sentences_only('See on esimene - ä lause. See, on teine: lause! see ei ole lause. Aga kas see on? jah, oli.'))  # ['See', 'on', 'esimene', 'ä', 'lause', 'See', 'on', 'teine', 'lause', 'Aga', 'kas', 'see', 'on']
print(find_years("1998sef672387fh3f87fh83777f777f7777f73wfj893w8938434343"))  # [1998, 7777]
print(find_phone_numbers("+372 56887364  +37256887364  +33359835647  56887364"))  # {'+372': ['56887364', '56887364'], '+333': ['59835647'], '': ['56887364']}
