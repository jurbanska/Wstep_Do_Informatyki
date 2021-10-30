l1 = int(input('Podaj dolna granice przedzialu: '))
l2 = int(input('Podaj gorna granice przedzialu: '))
wielkosc_zakresu = l2 - l1
srednia = int((l2 - l1) / 2)

if wielkosc_zakresu <= 20:
   while l1 <= l2:
       print(l1)
       l1 += 1
else:
    for i in range(srednia - 3, srednia + 4):
        if i != srednia:
            print(i)








