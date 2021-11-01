import random

pytanie = 'T'

while pytanie == 'T':
    liczba1 = int(input('Podaj pierwsza liczbe: '))
    liczba2 = int(input('Podaj druga liczbe: '))
    znak = input('Jakie działanie chcesz wykonac? - wpisz znak (+, -, *, /, **(potegowanie), ^(pierwiastkowanie), '
                 'x(losowanie liczby)): ')

    if znak == '+':
        print(liczba1, ' + ', liczba2, ' = ', liczba1 + liczba2)
    if znak == '-':
        print(liczba1, ' - ', liczba2, ' = ', liczba1 - liczba2)
    if znak == '*':
        print(liczba1, ' * ', liczba2, ' = ', liczba1 * liczba2)
    if znak == '/':
        print(liczba1, ' / ', liczba2, ' = ', liczba1 / liczba2)
    if znak == '**':
        print(liczba1, ' ** ', liczba2, ' = ', liczba1 ** liczba2)
    if znak == '^':
        print(liczba1, ' ^ ', liczba2, ' = ', liczba1 ** (1/liczba2))
    if znak == 'x':
        print('Losowa liczba z przedzialu ', '[', liczba1, ',', liczba2, '] to: ', random.randint(liczba1, liczba2))

    pytanie = input('Czy chcesz wprowadzic nowe dane? (T/N): ')
