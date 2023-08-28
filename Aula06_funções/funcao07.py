import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Argumentos Nomeados

def imprimir_nome(nome, sobrenome, idade):
  print("nome: ", nome)
  print("sobrenome: ", sobrenome)
  print("idade: ", idade)

nome = "João"
sobrenome = "Silva"
idade = 30

imprimir_nome(nome=nome, sobrenome=sobrenome, idade=idade)




