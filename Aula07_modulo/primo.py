import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Descubra se o número é primo
import math

def verificar_primo(numero):
  if numero <= 1:
    return ("Esse número não é primo: número menor ou igual a 1")
  elif numero == 2:
    return "Esse número é primo"
  elif numero % 2 == 0:
    return "Esse número não é primo"
  else:
    is_primo = True
    limite = int(math.sqrt(numero)) + 1
    for x in range(3, limite, 2):
      if numero % x == 0:
        is_primo = False
        break
    
    if is_primo:
      return "Esse número é primo"
    else:
      return "Esse número não é primo"






















  
  




