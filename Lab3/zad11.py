import statistics


def statystyki(lista):
    mediana = statistics.median(lista)
    srednia = statistics.mean(lista)
    min_val = min(lista)
    max_val = max(lista)
    odchylenie = statistics.stdev(lista)

    return mediana, srednia, min_val, max_val, odchylenie
