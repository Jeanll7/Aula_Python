import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Descubra se um numero é primo")

# Código AI

# def is_prime(number):
#   if number <= 1:
#     return False
#   for i in range(2, int(number**0.5) + 1):
#     if number % i == 0:
#       return False
#   return True

# # Solicitando um input do usuário
# numero = int(input("Digite um número inteiro: "))

# # Verificando se o número é primo e exibindo o resultado
# if is_prime(numero):
#   print(f"{numero} é um número primo.")
# else:
#   print(f"{numero} não é um número primo.")

print(30 * "-")

numero = int(input("Insira um numero para descobrirse o mesmo é primo: "))

if numero > 1:
  for x in range(2, numero):
    if numero % x == 0:
      print(f"{numero} não é primo")
      break
  else: 
    print(f"{numero} é primo") 
else:
  print("Esse numero não é primo: numero menor ou igual a 1")
  
print(30 * "-")
      
  
