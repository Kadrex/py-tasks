"""Yes."""


def no_fac(num: int) -> list:
    """
    Given integer num, return a list of numbers.

    The list should contain of all integers that are smaller than the given number
    and that are not factorials of any number.

    Factorial of a number is the product of multiplying each number, starting from 1 to that number (inclusive).
    Examples of factorial:
    0! = 1  (it just is that way, don't ask me why)
    1! = 1
    2! = 1 * 2 = 2
    3! = 1 * 2 * 3 = 6
    4! = 1 * 2 * 3 * 4 = 24
    Et cetera.

    Examples:
    no_fac(3) => [0]
    no_fac(4) => [0, 3]  Why not 1 and 2? Because 1! = 1 and 2! = 2
    no_fac(5) => [0, 3, 4]
    no_fac(10) => [0, 3, 4, 5, 7, 8, 9]  Because 1! = 1, 2! = 2 and 3! = 6
    no_fac(25) => [0, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 21, 23]  4! = 24

    :param num: given number
    :return: list of integers
    """
    factorials = [1]
    for i in range(1, num):
        factorials.append(factorials[-1] * i)
        if factorials[-1] >= num:
            break
    return [x for x in range(num) if x not in factorials]


if __name__ == '__main__':
    print(no_fac(25))
