import sys
sys.stdout.reconfigure(encoding='utf-8')

# do while

# Código para adivinhar um número

# codigo AI  < ================================================================= >

# numero = 9
# palpite = 0

# while True:
#   palpite_str = input("Digite seu palpite: ")

#   if not palpite_str.isdigit():
#     print("Erro: Digite um número inteiro.")
#     continue

#   palpite = int(palpite_str)

#   if palpite == numero:
#     print("Parabéns! Você adivinhou o número correto:", numero)
#     break
#   elif palpite < numero:
#     print("Tente um número maior.")
#   else:
#     print("Tente um número menor.")

# codigo Meu < ================================================================= >

palpite = 0
numero = 9

while True:
  print("Adivinhe o numero correto?")
  palpite = int(input())
  if palpite == numero:
    print("Parabéns você acertou")
    break
  else:
    print("Você errou")
else:
  print("Erro na aplicação")
  print(bool(palpite))
