import os

# Abrir um arquivo para leitura
with open('arquivo.txt', 'r') as arquivo:
  # Ler todo o conteúdo do arquivo para uma string
  dados = arquivo.read()
  print(dados)

with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
  dados = arquivo.read()
  print(dados)
  
# with open('arquivo.txt', 'r') as arquivo:
#   # Ler os primeiros 100 caracteres do arquivo
#   primeira_parte = arquivo.read(100)
#   print(primeira_parte)
  
  
