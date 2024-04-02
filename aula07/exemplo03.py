qtd = 0
frase = input("Digite uma frase: ")
for letra in frase:
     if (letra == "a") or (letra == "A") or (letra == "ã") or (letra == "Ã"):
      qtd = qtd + 1
print(f"Sua frase tem {qtd} letras A")