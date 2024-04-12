# -*- parser: babel -*-

n = int(input("Digite um número natural: "))

quadrado = 0

for i in range(1, n + 1):

    numero_impar = 2 * i - 1
    
    quadrado += numero_impar

print(f"O quadrado de {n} é {quadrado}.")
