a = input("wprowadz dane: ")

try:
    int_val = int(a)
    print("int")
except ValueError:
    try:
        float_val = float(a)
        print("float")
    except ValueError:
        if a.lower() in ("true", "false"):
            print("bool")
        else:
            print("string")
