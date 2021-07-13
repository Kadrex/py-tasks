"""Binary boss."""

import string
import re


class BinaryBoss:

    def __init__(self, decoding_file_name):
        self.decoding_dict = {}
        self.create_decoding_dict_from_file(decoding_file_name)

    def create_decoding_dict_from_file(self, filename: str) -> None:
        with open(filename, 'r') as file:
            for line in file.readlines():
                p1, p2 = self.get_key_and_val(line.rstrip('\n'))
                self.decoding_dict[int(p1)] = p2

    def get_key_and_val(self, line: str):
        for match in re.finditer(r'^(\d+) (.+)', line):
            return match.group(1), match.group(2)

    def convert_binary_to_int(self, binary_value: str) -> int:
        # return sum([int(binary_value[::-1][i]) * (2 ** i) for i in range(len(binary_value))])
        int_value = 0
        encoded_letter_reversed = binary_value[::-1]
        for i in range(len(binary_value)):
            int_value += int(encoded_letter_reversed[i]) * (2 ** i)
        return int_value

    def decode_symbol(self, encoded_symbol: str) -> str:
        return self.decoding_dict[self.convert_binary_to_int(encoded_symbol)]

    def decode_line(self, encoded_line: str) -> str:
        return ''.join([self.decode_symbol(encoded_symbol) for encoded_symbol in encoded_line.split(' ')])

    def decode_file(self, encoded_file_name, output_filename):
        with open(encoded_file_name, "r") as file:
            encoded_lines = [line.rstrip('\n') for line in file.readlines()]
        decoded_lines = [self.decode_line(line) for line in encoded_lines]
        with open(output_filename, "w") as file:
            file.writelines('\n'.join(decoded_lines))


def create_alphabet_dict() -> dict:
    x = {}
    uppercase_start_index = 65
    lowercase_start_index = 97
    for i in range(26):
        x[uppercase_start_index + i] = string.ascii_uppercase[i]
        x[lowercase_start_index + i] = string.ascii_lowercase[i]
    return x


def create_binary_key_file(filename: str):
    # from 32 to 126
    with open(filename, 'w') as file:
        for i in range(32, 127):
            file.write(f"{i} {chr(i)}\n")


if __name__ == '__main__':
    create_binary_key_file('binary_key.txt')
    binary_boss = BinaryBoss('binary_key.txt')
    print(binary_boss.decode_symbol('01000111'))
    print(binary_boss.decode_line('01001000 01100101 01101100 01101100 01101111'))
    binary_boss.decode_file('encoded_text.txt', 'output.txt')
