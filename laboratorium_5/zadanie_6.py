liczba = int(input("Podaj liczbe: "))

if liczba < 2:
    print("Liczba nie jest pierwsza")
    exit()

for i in range(2, int(liczba ** (1/2))):
    if (liczba % i) == 0:
        print("złożona")
        exit()
print("pierwsza")
