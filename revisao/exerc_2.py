def ler_listas(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        num_listas = int(linhas[0])
        listas = [linha.strip().split() for linha in linhas[1:]]
    return listas

def elementos_unicos(listas):
    elementos_unicos = []
    for lista in listas:
        contador = {}
        for elemento in lista:
            contador[elemento] = contador.get(elemento, 0) + 1
        unicos = [elemento for elemento, contagem in contador.items() if contagem == 1]
        elementos_unicos.append(unicos)
    return elementos_unicos

def contagem_ocorrencias(listas):
    contador_global = {}
    for lista in listas:
        for elemento in lista:
            contador_global[elemento] = contador_global.get(elemento, 0) + 1
    return contador_global

def diferenca_entre_listas(lista1, lista2):
    return set(lista2) - set(lista1)

def escrever_respostas(elementos_unicos, contagem, diferenca):
    with open("listasSaida.txt", "w") as arquivo_saida:
        arquivo_saida.write("Elementos únicos por lista:\n")
        for i, lista_unicos in enumerate(elementos_unicos, start=1):
            arquivo_saida.write(f"Lista {i}: {', '.join(lista_unicos)}\n")
        
        arquivo_saida.write("\nContagem de ocorrências de cada elemento:\n")
        for elemento, contagem in contagem.items():
            arquivo_saida.write(f"{elemento}: {contagem}\n")
        
        arquivo_saida.write("\nElementos na última lista, mas não na primeira:\n")
        arquivo_saida.write(", ".join(diferenca))

if __name__ == "__main__":
    listas = ler_listas("listas.txt")
    unicos_por_lista = elementos_unicos(listas)
    contagem = contagem_ocorrencias(listas)
    
    elementos_ultima_lista = listas[-1]
    elementos_primeira_lista = listas[0]
    diferenca = diferenca_entre_listas(elementos_primeira_lista, elementos_ultima_lista)
    
    escrever_respostas(unicos_por_lista, contagem, diferenca)
    print("Respostas escritas no arquivo 'listasSaida.txt'")