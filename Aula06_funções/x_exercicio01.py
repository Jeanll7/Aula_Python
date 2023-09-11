import sys
sys.stdout.reconfigure(encoding='utf-8') 

"""01 - Escreva um programa em que sejam lidos dois números reais, X e Y, e sejam feitas
chamadas a funções descritas abaixo, que deverão ser implementadas. No escopo global
deve ser impresso o resultado retornado por estas funções.
a) Uma função que receba X e Y como entrada e retorne o maior deles;
b) Uma função que receba X e Y como entrada e retorne a média aritmética deles;"""

# Função para encontrar o maior número entre X e Y
def find_larger(x, y):
  if x > y:
    return x
  else: 
    return y
  
# Função para calcular a média aritmética entre X e Y
def calculate_mean(x, y):
  if x == y:
    return f"X e Y são iguais: {x}"
  else:
    return (x + y) / 2

# Função principal
def main():
  x = float(input("Digite o primeiro número (X): "))
  y = float(input("Digite o segundo número (Y): "))
  
  largest = find_larger(x, y)
  mean = calculate_mean(x, y)
  
  print(f"O maior número entre X e Y é: {largest}")
  print(f"O média aritmética de X e Y é: {mean}")
  
main()

  



