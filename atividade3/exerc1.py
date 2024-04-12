frase = input("Digite uma frase para contar as letras:")
l = {}
for letra in frase:
    l[letra] = l.get(letra, 0) + 1
print(l)