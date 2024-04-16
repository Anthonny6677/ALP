from random import randint

n = []
l = []
for y in range(5):
    for x in range(5):
        l.append(randint(1,100))
    n.append(l)
    l = []

print(n)
soma = 0
for i in range(4):
    soma = soma + n[i][i]
print(f"{soma=}")