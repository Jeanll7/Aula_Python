# Jogo de adivinhação onde o computador escolhe um número e o jogador tenta adivinhar.

import random

numero_secreto = random.randint(1, 60) # numeros do sorteio
tentativas = 0

print("Bem-vindo ao jogo de adivinhação!")
while True:
  tentativa = int(input("Digite um número de 1 a 60: "))
  tentativas += 1
  if tentativa < numero_secreto:
    print("Tente um número maior.")
  elif tentativa > numero_secreto:
    print("Tente um número menor.")
  else:
    print(f"Parabéns! Você acertou em {tentativas} tentativas.")
    break




