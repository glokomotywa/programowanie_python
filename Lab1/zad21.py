a = 123
lista = []

while a != 0:
    lista.append(a % 10)
    a = a // 10

print(f'cyfra jednosci: {lista[0]}\ncyfra dziesiatek: {lista[1]}\ncyfra setek: {lista[2]} ')