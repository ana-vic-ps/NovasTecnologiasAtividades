V = [9, 8, 7, 12, 0, 13, 21]

valores_pares = []
valores_impares = []

for valor in V:
    if valor % 2 == 0:  
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)

print("Valores pares:", valores_pares)
print("Valores ímpares:", valores_impares)
