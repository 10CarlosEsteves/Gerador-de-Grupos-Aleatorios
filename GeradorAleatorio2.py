import GeradorDeGrupos

nomes=[]
gruposEmbaralhados=[]
arquivoDeBusca = ""
qtdDeGrupos = 0

print("\n\n")
print("------------------------------------------------------------------------")
arquivoDeBusca = input("Por favor, diga o nome (ou o caminho) do arquivo .csv: ")
qtdDeGrupos = int(input("Por favor, insira a quantidade de grupos que deseja formar: "))

nomes = GeradorDeGrupos.ExtrairNomes(arquivoDeBusca+".csv", nomes)
grupoEmbaralhado = GeradorDeGrupos.GerarGrupos(nomes, qtdDeGrupos)

GeradorDeGrupos.MostrarListaAleatoria(grupoEmbaralhado)
