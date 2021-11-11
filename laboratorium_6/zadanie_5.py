liczba = input("Podaj liczbe: ")
i = 0
j = len(liczba) - 1

if len(liczba) == 1:
    print("Liczba jest palindromem")

if len(liczba) % 2 == 0:  # jesli liczba ma parzysta ilosc cyfr oraz dzieli sie przez 11, to w systemie dziesietnym jest palindromem
    if int(liczba) % 11 == 0:
        print("Liczba jest palindromem")
    else:
        print("Liczba nie jest palindromem")
else:
    while i < len(liczba) / 2 < j:
        if liczba[i] == liczba[j]:
            i += 1
            j -= 1
            print("Liczba jest palindromem")
            exit()
        else:
            print("Liczba nie jest palindromem")
            exit()


#binarnie = bin(int(liczba))[2:] #ucinam przedrostek '0b', gdyz python tak zapisuje l. binarna