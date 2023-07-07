import os
import GeradorDeGrupos

os.system("cls")

nomes = []
grupos_embaralhados = []
arquivo = "veteranos.csv"
numero_grupos = 4

nomes =  GeradorDeGrupos.extrair_nomes(arquivo)
grupos_embaralhados = GeradorDeGrupos.gerar_grupos(nomes, numero_grupos)
GeradorDeGrupos.mostrar_grupos(grupos_embaralhados)
