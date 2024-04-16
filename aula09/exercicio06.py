from random import randint
resultados = [0] * 13
freq = [0] * 13

for _ in range(30000):
    dado1 = randint(1,6)
    dado2 = randint(1, 6)
    total = dado1 + dado2
    resultados[total] = resultados[total] + 1

for i in range(2,13):
    freq[i] = resultados[i] / 30000 * 100

for i in range(2,13):
    print(f"{i} - {resultados[i]} - {freq[i]:6.2f}%")