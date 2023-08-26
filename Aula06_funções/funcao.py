import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Paradigma imperativo
nome = "Jean"

def minhafuncao():
  global nome
  print(f"Olá, meu nome é {nome}")

minhafuncao()
  
nome = "Gabriel"

def minha_funcao_leitura():
  nome = "Jean"
  
  print(f"Olá, meu nome é {nome}")
  if nome == "Jean":
    print("Impressão do bloco interno da condição if")

minha_funcao_leitura()



















  
  




