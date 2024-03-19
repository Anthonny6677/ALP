a = float(input("Qual é o valor do lado A? "))
b = float(input("Qual é o valor do lado B? "))
c = float(input("Qual é o valor do lado C? "))
if  ((a + b)<c) or ((b + c)<a) or ((a + c)<b):
        print("Isso é um triangulo!")
elif (a == b == c):
        print("Isso é um triangulo equilatero!")
elif (a == b) or (a == c) or (b == c):
        print("Isso é um triangulo isosceles")
elif (a != b) or (a != c) or (b != c):
        print("Isso é um triangulo escaleno")
else:
        print("Isso não é um triangulo")
