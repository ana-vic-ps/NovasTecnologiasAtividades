lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

valores_comuns = conjunto1.intersection(conjunto2)
print("Valores comuns às duas listas:", valores_comuns)

valores_apenas_na_primeira = conjunto1.difference(conjunto2)
print("Valores que só existem na primeira lista:", valores_apenas_na_primeira)

valores_apenas_na_segunda = conjunto2.difference(conjunto1)
print("Valores que só existem na segunda lista:", valores_apenas_na_segunda)

elementos_unicos = list(conjunto1.union(conjunto2))
print("Elementos não repetidos das duas listas:", elementos_unicos)

lista1_sem_repetidos_na_segunda = list(conjunto1.difference(conjunto2))
print("Primeira lista sem os elementos repetidos na segunda:", lista1_sem_repetidos_na_segunda)
