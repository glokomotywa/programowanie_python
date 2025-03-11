def szukajWLiscie(lista, a):
    if isinstance(a, (int, float)):
        wystapienia = lista.count(a)
    elif isinstance(a, str):
        try:
            a = float(a)
            wystapienia = lista.count(a)
        except ValueError:
            a_sum = sum(ord(c) for c in a)
            wystapienia = lista.count(a_sum)
    elif isinstance(a, bool):
        wystapienia = lista.count(int(a))
    else:
        raise TypeError("Nieobsługiwany typ argumentu")

    print(f"Liczba wystąpień liczby {a}: {wystapienia}")
    return wystapienia
