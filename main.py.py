"""
gaseste ultimul nr prim mai mic decat numarul dat.
problema 1
"""


def get_largest_prime_below(n):
    nr = n - 1
    nuprime = 0
    ok = True

    while ok:
        for divizor in range(2, nr):
            if nr % divizor == 0:
                nuprime = nuprime + 1

        if nuprime == 0:
            return nr
        else:
            nr = nr - 1
            nuprime = 0


def test_get_largest_below():
    assert get_largest_prime_below(50) == 47
    assert get_largest_prime_below(100) == 97
    assert get_largest_prime_below(80) == 79


# Problema 12 .
def get_perfect_squares(start: int, end: int) -> list[int]:
    lista = []
    for i in range(start, end + 1):
        j = 1
        verificare = False
        while j * j <= i and not verificare:
            if i % j == 0 and i // j == j:
                verificare = True
            j += 1
        if verificare:
            lista.append(i)
    return lista


def test_get_perfect_squares():
    assert get_perfect_squares(1, 16) == [1, 4, 9, 16]
    assert get_perfect_squares(0, 5) == [1, 4]
    assert get_perfect_squares(16, 25) == [16, 25]


# Problema 5
def is_palindrome(n) -> bool:
    a = n
    invers = 0

    while n != 0:
        invers = invers * 10 + n % 10
        n = n // 10
    if invers == a:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(7777) == True
    assert is_palindrome(121) == True
    assert is_palindrome(100001) == True


def main():
    a = input("""
    Alegeti:
    1. Sa gasesti ultimul nr prim mai mic decat numarul dat.
    2. Sa se afle toate patratele perfect dintr un interval inchis.
    3. Sa se afle dacă un număr dat este palindrom.
    4. Poti iesi
    """)
    while a != '4':
        if a == '1':
            test_get_largest_below()
        elif a == '2':
            test_get_perfect_squares()
        elif a == '3':
            test_is_palindrome()
        a = input("""
    Alegeti:
    1. Sa gasesti ultimul nr prim mai mic decat numarul dat.
    2. Sa se afle toate patratele perfect dintr un interval inchis.
    3. Sa se afle dacă un număr dat este palindrom.
    4. Poti iesi
    """)


if __name__ == '__main__':
    main()
