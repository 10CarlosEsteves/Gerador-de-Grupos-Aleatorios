# Use nomes descritivos nas suas libs, não consigo identificar o que isso faz pelo nome
import Rian

# Ao iniciar uma variável de lista, não precisa dizer que é uma lista, apenas use um nome descritivo e deixe indicado, ex.: nomes e nomesEmbaralhados;
# Ao colocar no plural já vai estar indicado que é uma lista
listaDeNomes=[]
listaAleatoria=[]

# Nome de variável inicia com letra minúscula
# No Python, seja direto ao inicar a variável, inicie-a com seu valor padrão, ex.: nomeArquivo = "" e quantidadeGrupos = 0
ArquivoDeBusca = str()
qtdDeGrupos = int(0)

print("\n\n")
print("------------------------------------------------------------------------")

# Não quero ter que colocar .csv no final do input, você já diz que vou inserir um arquivo do tipo .csv, então é desnecessário
ArquivoDeBusca = input("Por favor, diga o nome (ou o caminho) do arquivo .csv: ")
qtdDeGrupos = int(input("Por favor, insira a quantidade de grupos que deseja formar: "))

listaDeNomes = Rian.ListaComNomes(ArquivoDeBusca, listaDeNomes)
listaAleatoria = Rian.GeradorAleatorio(listaDeNomes, qtdDeGrupos)

Rian.PrintListaAleatoria(listaAleatoria, qtdDeGrupos)
