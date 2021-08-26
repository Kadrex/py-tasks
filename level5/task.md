# EX Regex

### Lingid
- Regex: https://pydoc.pages.taltech.ee/extra/regex.html

## Ülesanne
Fail Gitis: `EX/ex...`

### I osa
Esimene osa koosneb lihtsatest regexiga
lahendatavatest funktsioonidest.

`def find_words(text: str) -> list` - funktsioon, mis saab sisendiks
sõne ``text`` ja tagastab järjendi selle sõne kõikidest sõnadest.
Sõnadeks loeme selles funktsioonis niisuguseid täheühendeid, mis
algavad ühe suure tähega ning koosnevad veel vähemalt ühest (aga võib
ka rohkemast) väiksest tähest. Tähed võivad olla ka täpitähed.
Sõnade leidmiseks tuleb kasutada regexit.

``def find_words_with_vowels(text: str) -> list`` - funktsioon, mis saab sisendiks
sõne ``text`` ja tagastab järjendi selle sõne kõikidest sõnadest,
mis algavad täishäälikuga.
Sõnadeks loeme selles funktsioonis niisuguseid täheühendeid, mis
algavad ühe suure tähega ning koosnevad veel vähemalt ühest (aga võib
ka rohkemast) väiksest tähest. Tähed võivad olla ka täpitähed.
Sõnade leidmiseks tuleb kasutada regexit.

``def find_sentences(text: str) -> list:`` - funktsioon, mis saab
sisendiks sõne ``text`` ja tagastab järjendi selle sõne kõikidest lausetest.
Lause algab alati suure tähega ja lõpeb lauselõpumärgiga (``.!?``).
Lause sees võivad olla sõnad, komad, koolonid, jutumärgid - kõik, mis tavalises lauseski.
Lausete leidmiseks tuleb kasutada regexit.

``def find_words_from_sentence(sentence: str) -> list`` - funktisoon, mis
saab sisendiks sõne ``sentence`` ja tagastab järjendi selle sõne kõikidest sõnadest.
Selles funktsioonis loeme sõnadeks tavalisi sõnu lausest, mis on eraldatud tühikuga.
Lause sees võivad olla ka komad ning teised kirjavahemärgid - neid ei tohi olla
tagastatavas sõnade järjendis, küll aga tuleb ka nende juures olevad sõnad järjendis
tagastada. Sõnade leidmiseks tuleb kasutada regexit.

``def find_words_from_sentences_only(text: str) -> list`` - funktsioon, mis saab
sisendiks sõne ``text`` ja tagastab järjendi selle sõne kõikide lausete kõikidest
sõnadest. Lause on defineeritud funktsioonis ``find_sentences()`` ning sõna
funktsioonis ``find_words_from_sentence()`` (wink-wink, kasutage olemasolevaid funktsioone).

``def find_years(text: str) -> list`` - funktsioon, mis saab sisendiks sõne ``text``,
mis koosneb suvalistest sümbolitest, ja tagastab järjendi selles sõnes esinevatest
aastaarvudest (täisarvud ehk int, mitte sõned) (aastaarvud saavad siin olla ainult neljakohalised).
Viiekohaline arv ei anna ei kaht ega üht aastaarvu välja. Aastaarvude leidmiseks tuleb kasutada regexit.

``def find_phone_numbers(text: str) -> dict`` - funktsioon, mis saab sisendiks sõne ``text``,
mis koosneb telefoninumbritest, ja tagastab sõnastiku selles sõnes esinevatest telefoninumbritest.
Telefoninumbril võib olla ees suunakood (suunakood koosneb plussist ja kolmest numbrist (näiteks `+372`),
suunakoodi võib telefoninumbrist eraldada tühik, aga ei pruugi). Telefoninumber ise on 7-8-kohaline.
Tagastava sõnastiku võtmeteks on suunakoodid ja väärtusteks järjendid nendest numbritest,
millel on antud suunakood. Need telefoninumbrid, millel pole suunakoodi ette antud, lähevad
sõnastikus tühja sõnega võtme alla. Telefoninumbrite ja suunakoodide leidmiseks tuleb kasutada regexit.

### II osa
Teises teeme natuke tutvust OOP-iga.
Olenevalt sellest, mis üllides OOP-iga
seni tehtud, tuleb siia mingi jutt.

Oletame, et sa oled juba viis aastat töötanud ühes tarkvarafirmas.
Ühel päeval võetakse sinu firmasse uus nooremarendaja/praktikant ning tal on olemas kõik õigused, k.a.
ligipääs ja muutmisõigus andmebaasile. Ta vaatab üht tabelit andmebaasis (nimega `entry`) ning
proovib aru saada, miks on selles tabelis kuus veergu andmete jaoks, kui need andmed saaks kõik kokku
ühte veergu panna. Niisiis kirjutab ta kavala SQL-lause ja kirjutab kõik andmed veergudest kokku ühte veergu
ning kustutab üleliigsed veerud ära. Sul on nüüd vaja sellest ühest veerust andmed välja õigesti välja lugeda.

Sul tuleb kirjutada funktsioon, mis saab sisendiks ühe rea (ehk siis ka ühe veeru - lihtsalt sõne) andmebaasist
ning teisendab selle rea objektiks Entry. Kuna praktikant ei leidnud seda klassi projektist üles, on see
sul olemas ja sa ei pea seda ise kirjutama.

Klass Entry:
```py 
class Entry:

    def __init__(self, first_name: str, last_name: str, date_of_birth: int, address: str):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address

    def __repr__(self) -> str:
        return f"Name: {self.first_name} {self.last_name}\nDate of birth: {self.date_of_birth}\nAddress: {self.address}"

    def __eq__(self, other) -> bool:
        """
        This method is perfect. Don't touch it.
        :param other:
        :return:
        """
        return self.first_name == other.first_name and self.last_name == other.last_name and \
               self.date_of_birth == other.date_of_birth and self.address == other.address

```

`def parse(row: str) -> Entry` - funktsioon, mis saab ette rea andmebaasist
ja tagastab objekti Entry vastavate parameetritega.


### Osa III - Schedule

Ha.