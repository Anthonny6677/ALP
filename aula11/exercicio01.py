lista = []
for x in range(10):
    numero = int(input(f"Digite o {x}o:"))
    lista.append(numero)

tupla = tuple(lista)
print(tupla[::-1])