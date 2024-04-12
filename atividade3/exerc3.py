def comparar_listas_versoes(inicial, alterada):
    conjunto_inicial = set(inicial)
    conjunto_alterada = set(alterada)

    nao_mudaram = conjunto_inicial.intersection(conjunto_alterada)

    novos_elementos = conjunto_alterada.difference(conjunto_inicial)

    removidos = conjunto_inicial.difference(conjunto_alterada)

    print("Elementos que não mudaram:", nao_mudaram)
    print("Novos elementos:", novos_elementos)
    print("Elementos removidos:", removidos)

lista_inicial = [1, 2, 3, 4, 5]

lista_alterada = [3, 4, 5, 6, 7]

# Comparar as duas versões
print("Comparação entre a versão inicial e a versão após alterações:")
comparar_listas_versoes(lista_inicial, lista_alterada)
