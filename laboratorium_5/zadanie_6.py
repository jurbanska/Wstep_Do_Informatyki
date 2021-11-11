liczba = int(input("Podaj liczbe: "))

if liczba < 2:
    print("Liczba nie jest pierwsza")
    exit()

for i in range(2, (liczba ** (1/2)) + 1):
    if (liczba % i) == 0:
        print("Liczba jest złożona")
        exit()
print("Liczba jest pierwsza")
