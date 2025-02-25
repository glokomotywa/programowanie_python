try:
    a = float(input("podaj a: "))
    b = float(input("podaj b: "))
    c = float(input("podaj c: "))

    if a != 0:
        delta = b**2 - 4*a*c
        if delta > 0:
            print("dwa miejsca zerowe")
        elif delta == 0:
            print("jedno miejsce zerowe")
        else:
            print("0 miejsc zerowych")

    else:
        print("zla funkcja (a=0)")
except ValueError:
    print("niepoprawne dane")