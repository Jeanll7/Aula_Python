import sys
sys.stdout.reconfigure(encoding='utf-8')

# Descobrir se o número é impar ou par

# Exemplo de uso: "menos avançado"

# def verificar_par_impar(numero):
#   if numero % 2 == 0:
#     return "par"
#   else:
#     return "ímpar"

# # Exemplo de uso:
# numero = int(input("Digite um número inteiro: "))
# resultado = verificar_par_impar(numero)
# print(f"O número {numero} é {resultado}.")

# <==============================================================================>

# numero = input("Insira um numero para saber se o mesmo é par: ")

# try:
#   numero_float = float(numero)
#   numero_int = int(numero_float)

#   if numero_float != numero_int:
#     print("Erro: O número inserido é fracionado.")
#   elif numero_int % 2 == 0:
#     print(f"{numero_int} é um número par.")
#   else:
#     print(f"{numero_int} é um número ímpar.")
# except ValueError:
#   print("Erro: Insira um número válido.")

# <==============================================================================>

print(60 * "-")

numero = int(input("Insira um numero para saber se o mesmo é par: "))
if (numero % 2) == 0:
  print(f"{numero} é um numero par")
else:
  print(f"{numero} é um numero impar")
print(60 * "-")

  
  


  
  
  
  