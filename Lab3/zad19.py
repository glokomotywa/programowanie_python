import math


def rysuj_figure(typ, *parametry):
    if typ == "kolo":
        r = parametry[0]
        print("Okrąg o promieniu", r)
        pole = math.pi * r ** 2
    elif typ == "kwadrat":
        bok = parametry[0]
        print("Kwadrat o boku", bok)
        pole = bok ** 2
    else:
        raise ValueError("Nieznany typ figury")

    print(f"Pole figury: {pole}")
