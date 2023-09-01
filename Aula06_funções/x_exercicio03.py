import sys
sys.stdout.reconfigure(encoding='utf-8') 

"""03 - Crie uma calculadora que consiga executar as funções destacadas da calculadora
padrão do windows 10"""

def somar(x, y):
  return x + y

def subtrair(x, y):
  return x - y

def multiplicar(x, y):
  return x * y

def dividir(x, y):
  if y == 0:
    return "Erro: Divisão por zero"
  return x / y

def main():
  while True:
    print("Opções:")
    print("Digite 'somar' para adição")
    print("Digite 'subtrair' para subtração")
    print("Digite 'multiplicar' para multiplicação")
    print("Digite 'dividir' para divisão")
    print("Digite 'sair' para encerrar o programa")

    escolha = input(": ")

    if escolha == "sair":
      break

    if escolha in ("somar", "subtrair", "multiplicar", "dividir"):
      num1 = float(input("Digite o primeiro número: "))
      num2 = float(input("Digite o segundo número: "))

      if escolha == "somar":
        resultado = somar(num1, num2)
      elif escolha == "subtrair":
        resultado = subtrair(num1, num2)
      elif escolha == "multiplicar":
        resultado = multiplicar(num1, num2)
      elif escolha == "dividir":
        resultado = dividir(num1, num2)

      print("Resultado:", resultado)
    else:
      print("Escolha inválida")

main()





