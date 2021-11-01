operacja = input('Co chcesz zrobic w kolejnym kroku - wplata/wyplata/saldo/zakoncz: ')
pin = input('Podaj pin: ') #pin ustawiony na 1234
saldo = 0

while operacja != 'zakoncz':
    if pin == '1234':
            if operacja == 'wplata':
                wplata = int(input('Podaj wplacana kwote: '))
                saldo = saldo + wplata

            if operacja == 'wyplata':
                wyplata = int(input('Podaj wyplacana kwote: '))
                if wyplata <= saldo:
                    saldo = saldo - wyplata
                else:
                    print('Nie posiadasz wystarczajacych srodkow na koncie, twoje saldo to: ', saldo)

            if operacja == 'saldo':
                print('Saldo: ', saldo)
    else:
        print('Nieprawidlowy PIN')

    operacja = input('Co chcesz zrobic w kolejnym kroku - wplata/wyplata/saldo/zakoncz: ')