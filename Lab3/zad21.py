import random


def kamien_papier_nozyce():
    opcje = ["kamień", "papier", "nożyce"]
    wybor_gracza = input("Wybierz kamień, papier lub nożyce: ")
    wybor_komputera = random.choice(opcje)

    if wybor_gracza == wybor_komputera:
        return "Remis!"

    if (wybor_gracza == "kamień" and wybor_komputera == "nożyce") or \
            (wybor_gracza == "papier" and wybor_komputera == "kamień") or \
            (wybor_gracza == "nożyce" and wybor_komputera == "papier"):
        return "Wygrałeś!"
    return "Przegrałeś!"
