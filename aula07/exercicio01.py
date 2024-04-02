n = int(input("Digite o valor do n: "))
e = 0
for i in range(1, n+1):
    e = e + 2**i
print(f"O valor de E = {e}")