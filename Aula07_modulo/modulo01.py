import sys
sys.stdout.reconfigure(encoding='utf-8') 

# from random import *

# print(randint(1, 30))

from random import randint

erros = 0
numero = randint(1, 10)

while True:
  print("Qual o numero correto? ")
  palpite = int(input())
  
  if palpite == numero:
    print("Parabéns você acertou")
    break
  else:
    # print("Tente novamente")
    erros += 1  

print(f"Você cometeu {erros} erro(s) durante a partida.")


 


  


















  
  




