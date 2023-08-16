import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Como achar o fatorial de um número")

# código AI

# def fatorial(n):
#   if n == 0 or n == 1:
#     return 1
#   else:
#     return n * fatorial(n - 1)

# Exemplo de uso:
# numero = 20
# resultado = fatorial(numero)
# print(f"O fatorial de {numero} é {resultado}.")

# <==============================================================================>

numero =int(input("Insira um numero: "))
fatorial = 1

if numero < 0:
  print("Não existe fatorial de numeros negativos")
elif numero == 0:
  print(f"O fatorial de {numero} é 1")
else:
  for x in range(1, numero+1):
    fatorial *= x

print(f"O fatorial de {numero} é {fatorial}")


