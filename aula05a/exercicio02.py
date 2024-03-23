nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
media = (nota1 + nota2) / 2

if 9 <= media <= 10:
    conceito = "A"

elif 7.5 <= media < 9:
    conceito = "B"

elif 6 <= media < 7.5:
    conceito = "C"

elif 4 <= media < 6:
    conceito = "D"

else: conceito = "E"

print("Sua media é:", media)
print("E seu conceito é:", conceito)