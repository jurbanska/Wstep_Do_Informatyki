# Napisz program, który utworzy i wypisze listę składającą się z N liczb z przedziału [1,100], a następnie po każdej
# liczbie pierwszej wstawi nowy element o wartości 0. Następnie program powinien policzyć sumy podzbiorów
# znajdujących się pomiędzy zerami. Lista przed modyfikacją: [7,45,45,34,53,45,4,3,11,18]. Lista po modyfikacji: [7,
# 0,45,45,34,53,45,4,3,0,11,0,18,30]. Wynik: 7;229;48
import random


def prime(liczba):
    if liczba < 2:
        return 0
        exit()

    for i in range(2, liczba):
        if (liczba % i) == 0:
            return 1
            exit()
    return 0


i = 0
liczby = []
N = int(input("Długość listy: "))

while i < N:
    liczby.insert(i, random.randint(1, 100))
    i += 1
print(liczby)

i = 0
while i < len(liczby):
    if prime(liczby[i]) == 0:
        liczby.insert(i + 1, 0)
        i += 2
    else:
        i += 1

print(liczby)
