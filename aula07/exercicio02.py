soma_altura = 0
soma_peso = 0
maior_imc = 0
menor_imc = 100
for i in range(1, 6):
    peso = float(input(f"Entre com o peso {i}: "))
    altura = float(input(f"Entre com a altura {i}: "))
    imc = peso / (altura * altura)
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc
        soma_altura = soma_altura + altura
        soma_peso = soma_peso + peso
media_peso = soma_peso / 5
media_altura = soma_altura / 5
print(f"O maior IMC é {maior_imc}")
print(f"O menor IMC é {menor_imc}")
print(f"A media dos pesos é {float(media_peso):.2f}kg \n")
print(f"A media das alturas é {float(media_altura):.2f}m \n")