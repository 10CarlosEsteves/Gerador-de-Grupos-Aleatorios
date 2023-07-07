import os
import GeradorDeGrupos

os.system("cls")

nomes = []
grupos_embaralhados = []
arquivo = ""
numero_grupos = 0

print("\n\n")
print("------------------------------------------------------------------------")
arquivo = input("Por favor, diga o nome (ou o caminho) do arquivo .csv: ")
numero_grupos = int(input("Por favor, insira a quantidade de grupos que deseja formar: "))

nomes = GeradorDeGrupos.extrair_nomes(arquivo + ".csv")
grupos_embaralhados = GeradorDeGrupos.gerar_grupos(nomes, numero_grupos)

GeradorDeGrupos.mostrar_grupos(grupos_embaralhados)
