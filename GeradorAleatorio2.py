import Rian

listaDeNomes=[]
listaAleatoria=[]
ArquivoDeBusca = str()
qtdDeGrupos = int(0)

print("\n\n")
print("------------------------------------------------------------------------")
ArquivoDeBusca = input("Por favor, diga o nome (ou o caminho) do arquivo .csv: ")
qtdDeGrupos = int(input("Por favor, insira a quantidade de grupos que deseja formar: "))

listaDeNomes = Rian.ListaComNomes(ArquivoDeBusca, listaDeNomes)
listaAleatoria = Rian.GeradorAleatorio(listaDeNomes, qtdDeGrupos)

Rian.PrintListaAleatoria(listaAleatoria, qtdDeGrupos)
