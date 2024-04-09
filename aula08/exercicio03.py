v = 0
frase = input("Digite a frase: ")
for vogais in "aeiouAEIOUãÃáÁàÀéÉèÈóÓÒíÍìÌêÊúÚùÙ":
    vogais = v + frase.count(vogais)
print(f"Sua frase tem {vogais} vogais")