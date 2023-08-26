import sys
sys.stdout.reconfigure(encoding='utf-8') 

# função em Python para verificar se um número é par ou ímpar

def par_impar(numero):
  if numero % 2 == 0:
    return "Par"
  else:
    return "Ímpar"

numero = 7
resultado = par_impar(numero)
print(f"O número {numero} é {resultado}.")

# ========================================
print('-'*40)

def par_impar(numero):
  
  if numero % 2 == 0:
    return "Numero Par"
  return "Numero Ímpar"

print(par_impar(4))


















  
  




