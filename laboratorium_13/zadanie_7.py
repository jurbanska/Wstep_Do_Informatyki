def pascal():
    for i in range(wiersze):
        trojkat.append([])
        trojkat[i].append(1)  # na pierwsze miejsce w wierszu wstawiamy 1
        for j in range(1, i):
            trojkat[i].append(trojkat[i - 1][j - 1] + trojkat[i - 1][j])
        if i != 0:
            trojkat[i].append(1)  # na ostatnie miejsce w wierszu wstawiamy 1
    return trojkat


def fibb():
    suma = 0
    i = wiersze / 2

    if wiersze == 1 or wiersze == 2:
        suma = 1
        print(suma)
        quit()

    if wiersze % 2 != 0:  # dla nieparzystej liczby wyrazów w wierszu
        for j in range(int(i), -1, -1):
            suma += trojkat[int(i)][j]
            i += 1
    if wiersze % 2 == 0:  # dla parzystej liczby wyrazów w wierszu
        for j in range(int(i - 1), -1, -1):
            suma += trojkat[int(i)][j]
            i += 1
    print(suma)


wiersze = int(input("Liczba wierszy: "))
trojkat = []

print(pascal())
(fibb())
