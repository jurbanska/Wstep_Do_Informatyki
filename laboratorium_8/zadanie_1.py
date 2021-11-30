# Napisz program, który utworzy i wypisze listę składającą się z N liczb z przedziału [1,100], a następnie po każdej
# liczbie pierwszej wstawi nowy element o wartości 0. Następnie program powinien policzyć sumy podzbiorów
# znajdujących się pomiędzy zerami. Lista przed modyfikacją: [7,45,45,34,53,45,4,3,11,18]. Lista po modyfikacji:
# [7,0,45,45,34,53,0,45,4,3,0,11,0,18]. Wynik: 7;177;52;11;18
import random


class NegativeNumberError(Exception):
    pass


def prime(liczba):  # funkcja sprawdzajaca, czy liczba jest pierwsza
    if liczba < 2:
        return 1  # liczba nie jest pierwsza

    for i in range(2, liczba):
        if (liczba % i) == 0:
            return 1
    return 0  # liczba jest pierwsza


i = 0
liczby = [7, 45, 45, 34, 53, 45, 4, 3, 11, 18]

try:
    N = int(input("Długość listy: "))
    if N <= 0:
        raise NegativeNumberError
except (ValueError, NegativeNumberError):
    print("Liczba nie jest całkowita dodatnia")
    exit()

while i < N:  # generowanie listy z losowymi liczbami z przedziału [1,100]
    liczby.insert(i, random.randint(1, 100))
    i += 1
print(liczby)

i = 0
while i < len(liczby):  # wstawianie 0 po każdej liczbie pierwszej
    if prime(liczby[i]) == 0:
        liczby.insert(i + 1, 0)
        i += 2
    else:
        i += 1
print(liczby)

if liczby[len(liczby) - 1] != 0:
    liczby.append(0)

suma = 0
wynik = []

for i in range(0, len(liczby)):  # sumowanie podzbiorów między zerami
    suma = liczby[i] + suma
    if liczby[i] == 0:
        wynik.append(suma)
        suma = 0


liczby.pop(len(liczby) - 1)
print(wynik)

'''
przykłady:
1) [7, 45, 45, 34, 53, 45, 4, 3, 11, 18] => [7, 0, 45, 45, 34, 53, 0, 45, 4, 3, 0, 11, 0, 18]
                                            =>[7, 177, 52, 11, 18]
2) [1, 15, 45, 13, 8, 7] => [1, 15, 45, 13, 0, 8, 7, 0] => [74, 15]
'''
