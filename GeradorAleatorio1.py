import Rian

listaDeNomes=[]
listaAleatoria=[]
qtdDeGrupos = int(0)

ArquivoDeBusca = "veteranos.csv"
qtdDeGrupos = 4

listaDeNomes =  Rian.ListaComNomes(ArquivoDeBusca, listaDeNomes)
qtdDeMembros = len(listaDeNomes)

"""
#Exibindo os nomes dos partipantes do escritório
print("Lista de Nomes de participantes do Escritório:")
for nome in listaDeNomes:
    print(f"-{nome}")
print(f"Tamanho total da lista: {qtdDeMembros}\n\n")
"""
listaAleatoria = Rian.GeradorAleatorio(listaDeNomes, 4)

Rian.PrintListaAleatoria(listaAleatoria, qtdDeGrupos)
