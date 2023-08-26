import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Variável global
idade = 30

# Função que recebe um argumento
def saudacao(nome):
  global idade  # Acessando a variável global idade
  print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

# Função que não recebe argumentos
def despedida():
  print("Até logo!")

# Chamada da função saudacao com argumento
saudacao("João")

# Chamada da função despedida
despedida()

# Modificando a variável global idade
idade = 25

# Chamada da função saudacao novamente
saudacao("Maria")


















  
  




