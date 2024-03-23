vhora = float(input("Digite o valor da hora trabalhada: "))
totalhr = float(input("Total de horas trablhadas: "))
slrbruto = vhora * totalhr

if slrbruto <= 900:
    ir = 0
    aliquota = 0

elif slrbruto <= 1500:
    ir = slrbruto * 0.05
    aliquota = 5

elif slrbruto <= 2500:
    ir = slrbruto * 0.1
    aliquota = 10

else: ir = slrbruto * 0.2 ; aliquota = 20

inss = slrbruto * 0.1
fgts = slrbruto * 0.11
sind = slrbruto * 0.03
totaldisc = ir + inss

slrliq = slrbruto - totaldisc

print("Salário bruto: (", vhora, "*", totalhr, ") :R$ ", slrbruto)
print("(-) IR (", aliquota, "%)                  : R$ ", ir)
print("(-) INSS (10%)                 : R$ ", inss)
print("FGTS (11%)                     : R$ ", fgts)
print("Total de descontos             : R$ ", totaldisc)
print("Salário Liquido                : R$ ", slrliq)