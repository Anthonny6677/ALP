n = int(input("Digite o valor do n: "))
e = 0
i = 1
while i <= n:
    e = e + 2**i
    i =i + 1
print(f"O valor de E = {e}")