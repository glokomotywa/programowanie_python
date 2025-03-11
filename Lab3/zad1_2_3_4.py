def pietro(znak):
    print(znak * 10)
    print(znak + " " * 8 + znak)
    print(znak * 10)

def dach(znak):
    for i in range(6):
        print(" " * (5 - i) + znak * (2 * i + 1))

def rysuj_dom(liczba_pieter, znak_dachu, znak_pietra):
    dach(znak_dachu)
    for _ in range(liczba_pieter):
        pietro(znak_pietra)


rysuj_dom(2, "*", "|")

