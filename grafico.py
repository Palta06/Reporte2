import time
import matplotlib.pyplot as plt
import random


def card_game(n, distribucion):
    cartas_A = [i+1 for i, c in enumerate(distribucion) if c == 'A']
    cartas_B = [i+1 for i, c in enumerate(distribucion) if c == 'B']

    while cartas_A and cartas_B:
        # Alice juega su carta más alta
        carta_A = max(cartas_A)
        # Bob responde con la carta más baja que pueda ganar
        posibles = [c for c in cartas_B if (c > carta_A) or (c == 1 and carta_A == n)]
        if posibles:
            carta_B = min(posibles)
            ganador = 'B'
        else:
            carta_B = min(cartas_B)
            ganador = 'A'

        cartas_A.remove(carta_A)
        cartas_B.remove(carta_B)

        if ganador == 'A':
            cartas_A.extend([carta_A, carta_B])
        else:
            cartas_B.extend([carta_A, carta_B])

    return "Alice" if cartas_A else "Bob"


n_values = list(range(2, 51))
tiempos = []

for n in n_values:
    distribucion = ['A'] * (n // 2) + ['B'] * (n - n // 2)
    random.shuffle(distribucion)

    repeticiones = 200  # para estabilizar medición
    inicio = time.time()
    for _ in range(repeticiones):
        card_game(n, distribucion)
    fin = time.time()
    tiempos.append((fin - inicio) / repeticiones)

# Gráfico
plt.plot(n_values, tiempos, marker='o')
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo de ejecución promedio (s)")
plt.title("Complejidad experimental - Card Game")
plt.grid(True)
plt.show()
