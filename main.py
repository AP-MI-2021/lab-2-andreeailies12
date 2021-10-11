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
    test_get_largest_below()
    test_get_perfect_squares()
    test_is_palindrome()

    a = input("""
    Alegeti:
    1. Citire numar.
    2. Sa gasesti ultimul nr prim mai mic decat numarul dat.
    3. Sa se afle toate patratele perfect dintr un interval inchis.
    4. Sa se afle dacă un număr dat este palindrom.
    5. Poti iesi
    """)

    while a != '5':
        if a == '1':
            nr = int(input('Citire numar'))
        elif a == '2':
            print(get_largest_prime_below(nr))
        elif a == '3':
            a = int(input('Alegeti inceputul intervalului: '))
            b = int(input('Alegeti sfarsitul intervalului: '))
            print(get_perfect_squares(a, b))
        elif a == '4':
            print(is_palindrome(nr))

        a = input("""
    Alegeti:
    1. Citire numar.
    2. Sa gasesti ultimul nr prim mai mic decat numarul dat.
    3. Sa se afle toate patratele perfect dintr un interval inchis.
    4. Sa se afle dacă un număr dat este palindrom.
    5. Poti iesi
    """)


if __name__ == '__main__':
    main()