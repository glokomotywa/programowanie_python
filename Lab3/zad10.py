def czy_wspolliniowe(P1, P2, P3):
    return (P2[1] - P1[1]) * (P3[0] - P2[0]) == (P3[1] - P2[1]) * (P2[0] - P1[0])


def obwodTrojkata(P1, P2, P3):
    if czy_wspolliniowe(P1, P2, P3):
        print("Punkty są współliniowe! Nie tworzą trójkąta.")
        return 0

    return obwodTrojkata(P1, P2, P3)
