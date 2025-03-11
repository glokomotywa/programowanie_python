import math

def odleglosc(P1, P2):
    return math.sqrt((P2[0] - P1[0]) ** 2 + (P2[1] - P1[1]) ** 2)

# Przykład:
P1 = [1, 2]
P2 = [4, 6]
print(odleglosc(P1, P2))
