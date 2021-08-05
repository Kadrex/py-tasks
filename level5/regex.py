"""
Andmebaasi salvestatud kujul
KadriMännimets02-12-1998Virula 8-1,Pärnumaa,Tori

Parse'i regexiga objektideks.
"""

import re


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


def parse(row: str) -> Entry:
    for match in re.finditer(r"([A-ZÕÄÖÜ]{1}[a-zõäöü]+)([A-ZÕÄÖÜ]{1}[a-zõäöü]+)(\d+-\d+-\d+)(.+)", row):
        name = match.group(1)
        name2 = match.group(2)
        time_of_birth = match.group(3)
        print(time_of_birth)
        for match2 in re.finditer(r"(\d+)-(\d+)-(\d+)", time_of_birth):
            print(f"Day: {match2.group(1)}, Month: {match2.group(2)}, Year: {match2.group(3)}")
        address = match.group(4)
        return Entry(name, name2, time_of_birth, address)


print(parse('KadriMännimets02-12-1998Virula 8-1,Pärnumaa,Tori'))
