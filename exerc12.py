def verificar_primo(numero):
    if numero > 1:
        for i in range(2, numero // 2 + 1):
            if numero % i == 0:
                return False
        else:
            return True
    else:
        return False
n = int(input("Digite o número de primos que deseja imprimir: "))

primos_encontrados = []
numero = 2 

while len(primos_encontrados) < n:
    if verificar_primo(numero):
        primos_encontrados.append(numero)
    numero += 1

print(f"Os primeiros {n} números primos são:")
print(primos_encontrados)
