import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Jogo Pedra Papel ou Tesoura
"""import random

def jogo_pedra_papel_tesoura(escolha_jogador):
  escolhas_possiveis = ["pedra", "papel", "tesoura"]
  
  if escolha_jogador not in escolhas_possiveis:
    return "Erro: Escolha inválida. Digite 'pedra', 'papel' ou 'tesoura'."
  
  escolha_computador = random.choice(escolhas_possiveis)

  print(f"Você escolheu: {escolha_jogador}")
  print(f"Computador escolheu: {escolha_computador}")

  if escolha_jogador == escolha_computador:
    return "Empate!"
  elif (
    (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
    (escolha_jogador == "tesoura" and escolha_computador == "papel") or
    (escolha_jogador == "papel" and escolha_computador == "pedra")
  ):
    return "Você ganhou!"
  else:
    return "Computador ganhou!"

escolha_do_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
resultado = jogo_pedra_papel_tesoura(escolha_do_jogador)
print(resultado)"""

# ======================================================================
import random

jogador_vitorias = 0
maquina_vitorias = 0

def Opcao_Jogador():
    while True:
        opcao = input("Escolha Pedra, Papel ou Tesoura: ").strip().lower()
        if opcao in ["pedra", "papel", "tesoura"]:
            return opcao
        else:
            print("Escolha inválida. Por favor, escolha Pedra, Papel ou Tesoura.")

while True:
    # Opções do jogo
    opcoes = ["pedra", "papel", "tesoura"]

    # Computador escolhe uma opção aleatória
    computador_escolha = random.choice(opcoes)

    # Solicita a escolha do jogador
    jogador_escolha = Opcao_Jogador()

    # Determina o vencedor
    if jogador_escolha == computador_escolha:
        print(f"Empate! Ambos escolheram {jogador_escolha}.")
    elif (jogador_escolha == "pedra" and computador_escolha == "tesoura") or \
         (jogador_escolha == "papel" and computador_escolha == "pedra") or \
         (jogador_escolha == "tesoura" and computador_escolha == "papel"):
        print(f"Você ganhou! {jogador_escolha.capitalize()} vence {computador_escolha}.")
        jogador_vitorias += 1
    else:
        print(f"Você perdeu! {computador_escolha.capitalize()} vence {jogador_escolha}.")
        maquina_vitorias += 1

    print(f"Placar - Você: {jogador_vitorias}, Máquina: {maquina_vitorias}")

    opcoes_jogador = input("Você quer jogar novamente? (sim/não): ").strip().lower()
    if opcoes_jogador in ["não", "nao", "n"]:
        break

# ======================================================================
# import random

# jogador_vitorias = 0
# maquina_vitorias = 0

# def Opcao_Jogador():
# #   variavel
#   opcao = input("Escolha Pedra, Papel oi Tesoura: ").lower() # .strip()
#   if opcao in ["pedra", "papel", "tesoura"]:
#     return opcao
#   else:
#     print("Escolha inválida. Por favor, escolha Pedra, Papel ou Tesoura.")
#     Opcao_Jogador()
  
  

# while True:
#   opcoes_jogador = ("Você quer jogar novamente? ")
#   if opcoes_jogador in ["SIM", "sim", "Sim", "s", "S" ]:
#     pass
#   elif opcoes_jogador in ["NAO", "nao", "Nao", "n", "N"]:
#     break
#   else:
    
    



















  
  




