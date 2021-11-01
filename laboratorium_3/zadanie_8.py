liczba = int(input('Podaj wysokosc choinki: '))
pien = liczba
n = 1

for i in range(0, liczba):
    print(liczba * " " + n * "*")
    liczba -= 1
    n += 2

print(pien * ' ' + 'U')
