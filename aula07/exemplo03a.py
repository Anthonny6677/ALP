qtd = 0
frase = input("Digite uma frase: ")
for letra in frase:
     if letra in "AEIOUaeiouãíéóu":
      qtd = qtd + 1
print(f"Sua frase tem {qtd} vogais")