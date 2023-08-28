import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Parâmetros de função

# def saudacao(nome):
#   print(f"Olá {nome}!")

# saudacao("Pedro")

"""def nome_da_funcao(params): # parâmetro é o nome dado aos valores ultilizados na definição de uma função
  # corpo da função
  print("Olá", params)
  
nome = input("Digite o seu nome? ")
nome_da_funcao(nome) # argumento é o nome dado aos valores ultilizados na chamada de uma função"""

# def imprime_nome(nome_completo):
#   print(f"Olá, {nome_completo}")

# nome = input("Qual seu nome? ")
# sobrenome = input("digite seu segundo nome: ")
# nome_completo = nome +" "+ sobrenome
# imprime_nome(nome_completo)

def imprime_nome(nome_completo):
  print(f"Olá, {nome_completo}")

def main():
  nome = input("Qual seu nome? ")
  sobrenome = input("Digite seu sobrenome: ")
  
  nome_completo = nome + " " + sobrenome
  imprime_nome(nome_completo)

if __name__ == "__main__":
  main()






  
  




