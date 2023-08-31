import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Função Recursão 1/2

"""def reduzir_numero(numero_int):
  while numero_int > 0:
    print(numero_int)
    numero_int -= 1
    
    
reduzir_numero(5)"""

# 1 - checar se o nosso numero não é igual a 0
# 2 - se ele não for igual a 0 - reduzir 1 unudade

"""def reduzir_numero(numero_int):
  while numero_int > 0:
    print("Valor atual:", numero_int) 
    if numero_int != 0:
      print("1 - Verificando se o número não é igual a 0...") 
    else:
      print("Número igual a 0, encerrado.")  
    numero_int -= 1 

reduzir_numero(5)  """

# 1 - checar se o nosso numero não é igual a 0
# 2 - se ele não for igual a 0 - reduzir 1 unudade

def reduzir_numero(numero_int):
  print(numero_int)  
  if numero_int > 0:
    reduzir_numero(numero_int - 1)    
    print(numero_int) 
    
    
reduzir_numero(5)
 





