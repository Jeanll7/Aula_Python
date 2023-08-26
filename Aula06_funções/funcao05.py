import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Jogo Pedra Papel ou Tesoura
# from random import choice

# jogador_vitorias = 0
# maquina_vitorias = 0

# def Opcao_Jogador():
#   while True:
#     opcao = input("Escolha Pedra, Papel ou Tesoura: ").lower()
#     if opcao in ["pedra", "papel", "tesoura"]:
#       return opcao
#     else:
#       print("Escolha inválida. Por favor, escolha Pedra, Papel ou Tesoura.")

# def Verifica_Vencedor(jogador, maquina):
#   if jogador == maquina:
#     return "Empate"
#   if (
#     (jogador == "pedra" and maquina == "tesoura")
#     or (jogador == "papel" and maquina == "pedra")
#     or (jogador == "tesoura" and maquina == "papel")
#   ):
#     return "Jogador"
#   return "Máquina"

# while True:
#   opcao_jogador = Opcao_Jogador()
#   escolha_maquina = choice(["pedra", "papel", "tesoura"])

#   print(f"Você escolheu: {opcao_jogador}")
#   print(f"A máquina escolheu: {escolha_maquina}")

#   vencedor = Verifica_Vencedor(opcao_jogador, escolha_maquina)

#   if vencedor == "Jogador":
#     jogador_vitorias += 1
#     print("Você venceu esta rodada!")
#   elif vencedor == "Máquina":
#     maquina_vitorias += 1
#     print("A máquina venceu esta rodada!")
#   else:
#     print("Ninguém venceu esta rodada. Empate!")

#   print(f"Placar: Jogador {jogador_vitorias} - Máquina {maquina_vitorias}")

#   opcoes_jogador = input("Você quer jogar novamente? (sim/não): ").lower()
#   if opcoes_jogador not in ["sim", "s"]:
#     break

# ======================================================================
"""from random import choice

vitorias_jogador = 0
vitorias_maquina = 0

def obter_escolha_jogador():
  while True:
    escolha = input("Escolha Pedra, Papel ou Tesoura: ").lower()
    if escolha in ["pedra", "papel", "tesoura"]:
      return escolha
    else:
      print("Escolha inválida. Por favor, escolha Pedra, Papel ou Tesoura.")

def obter_escolha_maquina():
  escolha_maquina = choice(["pedra", "papel", "tesoura"])
  return escolha_maquina

while True:
  escolha_jogador = obter_escolha_jogador()
  escolha_maquina = obter_escolha_maquina()

  print(f"Você escolheu: {escolha_jogador}")
  print(f"A máquina escolheu: {escolha_maquina}")
  
  # Determine o vencedor desta rodada e atualize os pontos.
  if escolha_jogador == escolha_maquina:
      print("Empate!")
  elif (
    (escolha_jogador == "pedra" and escolha_maquina == "tesoura")
    or (escolha_jogador == "papel" and escolha_maquina == "pedra")
    or (escolha_jogador == "tesoura" and escolha_maquina == "papel")
  ):
    print("Você venceu esta rodada!")
    vitorias_jogador += 1
  else:
    print("A máquina venceu esta rodada!")
    vitorias_maquina += 1

  print(f"Vitórias do Jogador: {vitorias_jogador}")
  print(f"Vitórias da Máquina: {vitorias_maquina}")

  jogar_novamente = input("Você quer jogar novamente? (sim/não): ").lower()
  if jogar_novamente != "sim":
    break"""

# ======================================================================
from random import choice

vitorias_jogador = 0
vitorias_maquina = 0
empates = 0

def escolha_jogador():
  escolha  = input("Escolha Pedra, Papel ou Tesoura: ").lower()
  if escolha  in ["pedra", "papel", "tesoura"]:
    return escolha 
  else:
    print("Escolha inválida. Por favor, escolha Pedra, Papel ou Tesoura.")
    escolha_jogador()
  
def escolha_maquina():
  escolha_maquina = choice(["pedra", "papel", "tesoura"])
  return escolha_maquina

while True: 
  escolha_j = escolha_jogador()
  escolha_m = escolha_maquina()
  
  print(f"Jogador escolheu {escolha_j} e a Máquina escolheu {escolha_m}")
  
  if (escolha_j == "pedra" and escolha_m == "tesoura") or \
    (escolha_j == "papel" and escolha_m == "pedra") or \
    (escolha_j == "tesoura" and escolha_m == "papel"):
    print("Resultado: Você Ganhou!")
    vitorias_jogador += 1
  elif escolha_j == escolha_m:
    print("Resultado: Empate!")
    empates += 1
  else:
    print("Resultado: Máquina Ganhou!")
    vitorias_maquina += 1

  print(f"Vitórias do Jogador: {vitorias_jogador}")
  print(f"Vitórias da Máquina: {vitorias_maquina}")
  print(f"Empates: {empates}")
    
  opcoes_jogador = input("Você quer jogar novamente? (sim/não): ").lower()
  if opcoes_jogador in ["n", "não", "nao", "NÃO", "NAO"]:
    break
 
    


















  
  




