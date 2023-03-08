import GeradorDeGrupos

nomes=[]
gruposEmbaralhados=[]
arquivoDeBusca = "veteranos.csv"
qtdDeGrupos = 4

nomes =  GeradorDeGrupos.ExtrairNomes(arquivoDeBusca, nomes)

gruposEmbaralhados = GeradorDeGrupos.GerarGrupos(nomes, qtdDeGrupos)

GeradorDeGrupos.MostrarListaAleatoria(gruposEmbaralhados)
