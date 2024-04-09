nascimento = input("Digite a data nascimento <DD/MM/AAAA>: ")
data = nascimento.split('/')
nasc = data[2] + data[1] + data[0]
print(f"A data é {nasc}")