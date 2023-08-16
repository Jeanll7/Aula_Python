import sys
sys.stdout.reconfigure(encoding='utf-8')

# chave = input("Digite a base da sua senha: ")

# senha = ""
# for letra in chave:
#  if letra in "Aa":
#   senha = senha + ""


# Solicita ao usuário que digite a base para a senha
chave = input("Digite a base da sua senha: ")

# Inicializa a variável 'senha' como uma string vazia
senha = ""

# Percorre cada caractere (letra) presente na string 'chave'
for letra in chave:
  # Verifica se a letra é 'A' ou 'a', e adiciona '10' à variável 'senha'
  if letra in "Aa": senha = senha + "10"
  elif letra in "Bb": senha = senha + "@"
  elif letra in "Cc": senha = senha + "2"
  elif letra in "Dd": senha = senha + "3"
  elif letra in "Ee": senha = senha + "4"
  elif letra in "Ff": senha = senha + "5"
  elif letra in "Rr": senha = senha + "#"
  elif letra in "Ss": senha = senha + "%"
  elif letra in "Mm": senha = senha + "$"
  # Caso contrário, ou seja, se a letra não corresponder a nenhum dos casos acima,
  # a própria letra é adicionada à variável 'senha'
  else:
    senha = senha + letra
# Imprime a senha final
print(senha)


  











