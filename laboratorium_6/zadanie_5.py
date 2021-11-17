# program sprawdzający,czy liczba jest palindromem w systemie dziesietnym i binarnym

class NegativeNumberError(Exception):
    pass


try:
    liczba = int(input("Podaj liczbe: "))
    if liczba < 0:
        raise NegativeNumberError
except (ValueError, NegativeNumberError):  # liczba musi byc naturalna
    print("Liczba nie jest naturalna")
    exit()

i = 0
j = len(str(liczba)) - 1
palindrom = False

if len(str(liczba)) == 1:
    print("Liczba jest palindromem w systemie dziesietnym")

if len(str(liczba)) % 2 == 0:
    if int(liczba) % 11 == 0:
        print("Liczba jest palindromem w systemie dziesietnym")
    else:
        print("Liczba nie jest palindromem w systemie dziesietnym")
else:
    while i < len(str(liczba)) / 2 < j:
        if str(liczba)[i] == str(liczba)[j]:
            palindrom = True
            i += 1
            j -= 1
        else:
            palindrom = False
            print("Liczba nie jest palindromem w systemie dziesietnym")
            break
if palindrom:
    print("Liczba jest palindromem w systemie dziesietnym")

binarnie = ""
while liczba != 0:
    binarnie = str(liczba % 2) + binarnie
    liczba = int(liczba / 2)
print("Liczba binarnie: ", binarnie)

i = 0
j = len(binarnie) - 1

if len(binarnie) == 1:
    print("Liczba jest palindromem w systemie binarnym")

if len(binarnie) % 2 == 0:
    while i <= ((len(binarnie) / 2) - 1) <= j:
        if binarnie[i] == binarnie[j]:
            i += 1
            j -= 1
        else:
            print("Liczba nie jest palindromem w systemie binarnym")
            quit()
    print("Liczba jest palindromem w systemie binarnym")

if len(binarnie) % 2 != 0:
    while i < len(binarnie) / 2 < j:
        if binarnie[i] == binarnie[j]:
            i += 1
            j -= 1
        else:
            print("Liczba nie jest palindromem w systemie binarnym")
            quit()
    print("Liczba jest palindromem w systemie binarnym")

# przykłady: 33(palindrom binarnie i dziesiętnie), 63(palindrom binarnie), 7759(palindrom binarnie), 12345678987654321
