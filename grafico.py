import time
import matplotlib.pyplot as plt
import random

def ganador_cartas(n, distribucion):
    # Algoritmo iterativo simplificado
    cartas_A = sum(1 for c in distribucion if c == 'A')
    cartas_B = n - cartas_A
    if cartas_A > cartas_B:
        return "Alice"
    else:
        return "Bob"

n_values = list(range(2, 51))
tiempos = []

for n in n_values:
    distribucion = ['A'] * (n // 2) + ['B'] * (n - n // 2)
    random.shuffle(distribucion)
    inicio = time.time()
    ganador_cartas(n, distribucion)
    fin = time.time()
    tiempos.append(fin - inicio)

plt.plot(n_values, tiempos, marker='o')
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo de ejecución (s)")
plt.title("Tiempo de ejecución del algoritmo Card Game")
plt.grid(True)
plt.show()
