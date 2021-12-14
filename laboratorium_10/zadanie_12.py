# Wykorzystując funkcje, proszę napisać program, który będzie konwertował znaki podawane przez użytkownika na znaki
# ASCII. Kody znaków powinny znajdować się w pliku i stamtąd powinny być pobierane.


def a(text):
    wynik = ''
    for k in range(0, len(text)):
        for line in code:  # sprawdzamy linijki w pliku kod.txt
            if text[k] in line:
                if line[len(line) - 2] == text[k]:
                    wynik += (line[:-2]) + " "
        code.seek(0)
    print(wynik)


code = open("kod.txt", "r")
a(text=input("Podaj zdanie: "))
code.close()

'''
Przyklady:
'komputer' => 107 111 109 112 117 116 101 114
'czy zdam matematyke za 1 razem?' => 99 122 121 32 122 100 97 109 32 109 97 116 101 109 97 116 121 107 101 32 122 97 32
 49 32 114 97 122 101 109 63
'''
