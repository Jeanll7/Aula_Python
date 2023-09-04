import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Verificar numeros primos

def is_prime(numero):
  if numero <= 1:
    return False
  elif numero <= 3:
    return True
  elif numero % 2 == 0 or numero % 3 == 0:
    return False
  i = 5
  while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
      return False
    i += 6
  return True

# Exemplos de uso:
numero = 15
if is_prime(numero):
  print(f"{numero} é primo")
else:
  print(f"{numero} não é primo")





















  
  




