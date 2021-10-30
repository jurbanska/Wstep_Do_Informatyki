l1 = int(input('Podaj liczbe nr1: '))
l2 = int(input('Podaj liczbe nr2: '))

'''
działania:
na l1 i l2
'''

suma = l1 + l2  # dodawanie liczby l1 i l2
print('Suma: ', suma)

roznica = l1 - l2  # odejmowanie liczby l1 i l2
print('Roznica: ', roznica)

iloczyn = l1 * l2  # mnozenie liczby l1 i l2
print('Iloczyn: ', iloczyn)

iloraz = l1 / l2  # dzielenie liczby l1 i l2
print('Iloraz: ', iloraz)

kwadrat_l1 = l1 ** 2  # kwadrat l1
print('Kwadrat l1: ', kwadrat_l1)

kwadrat_l2 = l2 ** 2  # kwadrat l2
print('Kwadrat l2: ', kwadrat_l2)

pierwiastek_l1 = l1 ** (1 / 2)  # pierwiastek l1
print('Pierwiastek z l1: ', pierwiastek_l1)

pierwiastek_l2 = l2 ** (1 / 2)  # pierwiastek l2
print('Pierwiastek z l2: ', pierwiastek_l2)

if (l1 < 0 and l2 > 0) or (l1 > 0 and l2 < 0):
    print('Wartosc bezwzgledna z ujemnej liczby to: ', abs(min(l1, l2)))

if (l1 and l2) < 0:
    exit(print('Obie liczby sa mniejsze od 0'))

if (l1 * l2):
    print("Yay!")

