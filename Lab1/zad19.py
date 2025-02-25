
try:
    a = float(input("podaj a: "))
    b = float(input("podaj b: "))

    if a != 0:
        x0 = -b / a
        print(f'miejsce zerowe: {x0}')
    elif b == 0:
        print("funkcja stala, nieskonczenie wiele miejsc zerowych")
    else:
        print("funkcja stala, brak miejsc zerowych")

except ValueError:
    print("podaj poprawne wartosci")