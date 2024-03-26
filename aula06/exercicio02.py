ValorDaCompra = float(input("Digite o valor da compra: "))

if ValorDaCompra <= 1000.00:
    desconto = ValorDaCompra - (ValorDaCompra * 0.10)
    print("O desconto é de 10% e o valor final do produto será de", desconto, "Reais")
elif ValorDaCompra <= 5000.00:
    desconto2 = ValorDaCompra - (ValorDaCompra * 0.20)
    print("O desconto é de 20% e o valor final do produto será de", desconto2, "Reais")
elif ValorDaCompra > 5000.00:
    desconto3 = ValorDaCompra - (ValorDaCompra * 0.30)
    print("O desconto é de 30% e o valor final do produto será de", desconto3, "Reais")
else: print("Desculpe, tente inserir um novo número")