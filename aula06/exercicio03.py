comprimento = float(input("Digite o comprimento: "))
altura = float(input("Digite a altura: "))
LataLitros = float(input("Quantos litros tem na lata que será utilizada? "))
porta = 1.68
pintura = (comprimento * altura) * 4 - porta
litros = pintura / 3
TotalLata = litros / LataLitros
print("A àrea total que será pintada é de ", pintura)
print("Será necessário", litros, "litros de tinta para pintar as paredes")
print("Será necessário", round(TotalLata), "latas de tinta para pintar as paredes")