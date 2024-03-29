# Proszę napisać program, który umożliwia zamianę dowolnej liczby naturalnej z jednego systemu liczb w drugi w
# zależności od wyboru użytkownika (na wejściu). Należy rozważyć następujące systemy liczbowe: dwójkowy, ósemkowy,
# dziesiętny, szesnastkowy.

class IdenticalNumberError(Exception):
    pass


try:
    system_1 = int(input("Wybierz system, z którego zamieniasz (2/8/10/16): "))
    system_2 = int(input("Wybierz system, na który zamieniasz (2/8/10/16): "))
    if system_1 == system_2:
        raise IdenticalNumberError
except IdenticalNumberError:
    print("Wymienione systemy są takie same")
    exit()

liczba = input("Podaj liczbę: ")

if system_1 == 2 or system_1 == 8:  # zamiana binarnego i oktalnego na dziesiętny
    j = 0
    i = len(liczba) - 1
    wynikdec = 0
    while i > -1:
        wynikdec = int(liczba[i]) * (system_1 ** j) + wynikdec
        j += 1
        i -= 1

if system_1 == 10:
    wynikdec = int(liczba)

if system_1 == 16:  # zamiana szesnastkowego na dziesiętny
    j = 0
    i = len(liczba) - 1
    k = 0
    wynikdec = 0
    lista = []

    while k < len(liczba):  # zapisanie liczby jako elementy listy
        lista.insert(k, liczba[k])
        k += 1

    while i > -1:
        if lista[i] == 'A':
            lista[i] = 10
        if lista[i] == 'B':
            lista[i] = 11
        if lista[i] == 'C':
            lista[i] = 12
        if lista[i] == 'D':
            lista[i] = 13
        if lista[i] == 'E':
            lista[i] = 14
        if lista[i] == 'F':
            lista[i] = 15

        wynikdec = int(lista[i]) * (16 ** j) + wynikdec
        j += 1
        i -= 1

if system_2 == 2 or system_2 == 8:  # zamiana z dziesiętnego na binarny lub oktalny
    wynik = ""
    while wynikdec > 0:
        wynik = str(wynikdec % system_2) + wynik
        wynikdec = int(wynikdec / system_2)
    print(wynik)

if system_2 == 10:
    print(wynikdec)

if system_2 == 16:  # zamiana z dziesiętnego na szesnastkowy
    cyfry = "0123456789ABCDEF"
    szesnastkowy = ""
    while wynikdec > 0:
        szesnastkowy = cyfry[wynikdec % 16] + szesnastkowy
        wynikdec = int(wynikdec / 16)
    print(szesnastkowy)

#przykłady: bin => hex: 111101 = 3D, hex => dec: 3D = 61, dec => okt: 61 = 75