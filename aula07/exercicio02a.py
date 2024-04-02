soma = 0
qtd = 0
for i in range(1, 6):
    peso = float(input(f"Entre com o peso {i}: "))
    altura = float(input(f"Entre com a altura {i}: "))
    qtd = qtd + 1
    soma1 = soma + peso
    soma2 = soma + altura
media1 = soma1 / qtd
media2 = soma2 / qtd
print(f"A media dos pesos é {float(media1)} kg")
print(f"A media das alturas é {float(media2)} m")