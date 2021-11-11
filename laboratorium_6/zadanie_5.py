liczba = input("Podaj liczbe: ")
i = 0
j = len(liczba) - 1

if len(liczba) == 1:
    print("Liczba jest palindromem w systemie dziesietnym")

if len(liczba) % 2 == 0:  # jesli liczba ma parzysta ilosc cyfr i dzieli sie przez 11, to w dziesietnym jest palindromem
    if int(liczba) % 11 == 0:
        print("Liczba jest palindromem w systemie dziesietnym")
    else:
        print("Liczba nie jest palindromem w systemie dziesietnym")
else:
    while i < len(liczba) / 2 < j:
        if liczba[i] == liczba[j]:
            i += 1
            j -= 1
            print("Liczba jest palindromem w systemie dziesietnym")
            break
        else:
            print("Liczba nie jest palindromem w systemie dziesietnym")
            break

binarnie = bin(int(liczba))[2:]  # ucinam przedrostek '0b', gdyz python tak zapisuje l. binarna
i = 0
j = len(binarnie) - 1

if len(binarnie) == 1:
    print("Liczba jest palindromem w systemie binarnym")

while i < len(binarnie) / 2 < j:
    if binarnie[i] == binarnie[j]:
        i += 1
        j -= 1
        print("Liczba jest palindromem w systemie binarnym")
        break
    else:
        print("Liczba nie jest palindromem w systemie binarnym")
        break
