def extrair_nomes(nome_arquivo):
    """Esta função extrai os nomes do arquivo .csv, armazena em uma lista e a retorna"""
    with open(nome_arquivo, encoding="UTF-8") as arquivo_csv:
        
        matriz = csv.reader(arquivo_csv, delimiter=",")

        for lista in matriz:
            nomes = [nome for nome in lista]
    return nomes


def gerar_grupos(nomes, num_grupos):
    """Esta função gera uma matriz de grupos aleatórios."""
    pessoas_por_grupo = len(nomes) // num_grupos
    
    grupos = []

    # distribuindo as pessoas exatas entre os grupos
    for indice in range(num_grupos):
        
        grupo = random.sample(nomes, pessoas_por_grupo)
        grupos.append(grupo) 
        
        for pessoa in grupo:
            nomes.remove(pessoa)

    # distribuindo os remanescentes entre os grupos
    while nomes:
        limite_por_grupo = pessoas_por_grupo + 1
        indice = random.randrange( num_grupos )

        if len(grupos[indice]) < limite_por_grupo:
            pessoa = nomes.pop()
            grupos[indice].append(pessoa)

    return grupos

def mostrar_grupos(grupos):
    """Esta função mostra os grupos e seus respectivos participantes"""
    for indice, grupo in enumerate(grupos):
        print("--------------------------------")
        print(f"PARTICIPANTES DO GRUPO {indice + 1}")
        for nome in grupo:
            print(f"-{nome} ")
        indice+=1
