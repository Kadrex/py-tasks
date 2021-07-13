"""Sharing is caring, friendship is magic."""


def cookies(num_of_cookies: int, num_of_friends: int) -> tuple:
    """
    You bought a pack of yummy Leibniz cookies and you want to share it with your friends.

    Given the amount of cookies in the pack and number of friends to share them with,
    write a function that returns how many cookies each friend gets.

    All your friends should get the same amount of cookies,
    you don't want them to feel that you like some more than others (even if you do, which is ok, btw).
    Although your friends should each get the same amount of cookies, you, however, can have less or more than them.
    The amount of cookies you get should be as close to the amount your friends get.
    If the difference between getting more or less cookies than your friends is the same, you should get less.

    The function should return tuple where first value is how many cookies each of your friend gets
    and the second value is how many cookies you get.

    cookies(23, 3) => (6, 5)  # It's (6, 5) (with diff=1) and not (7, 2) (with diff=5) and not (5, 8) (with diff=3)
    cookies(25, 3) => (6, 7)  # It's (6, 7) (with diff=1) and not (7, 4) (with diff=3) and not (5, 10) (with diff=5)
    cookies(76, 4) => (15, 16)
    cookies(75, 4) => (15, 15)  # Yay!
    cookies(13, 1) => (7, 6)  # It's (7, 6) and not (6, 7), because you should get less than your pals. Be nice.

    :param num_of_cookies: number of cookies in the pack
    :param num_of_friends: number of friends to share the cookies with
    :return: tuple, where first value is friends' cookies and second yours
    """
    cookies_per_ppl = num_of_cookies // (num_of_friends + 1)
    if cookies_per_ppl * (num_of_friends + 1) != num_of_cookies:
        extra_cookies = num_of_cookies - cookies_per_ppl * (num_of_friends + 1)
        hyp_friend_cookies = cookies_per_ppl + 1
        for_me = num_of_cookies - hyp_friend_cookies * num_of_friends
        if abs(hyp_friend_cookies - for_me) > extra_cookies:
            return cookies_per_ppl, cookies_per_ppl + extra_cookies
        return hyp_friend_cookies, for_me
    return cookies_per_ppl, cookies_per_ppl


if __name__ == '__main__':
    print(cookies(23, 3))
    print(cookies(25, 3))
    print(cookies(76, 4))
    print(cookies(75, 4))
    print(cookies(13, 1))
