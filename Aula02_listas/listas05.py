import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Funções (list) 

nome = "Curso de Python"
valor = range(10)

print(nome)
print(valor)

lista7 = list(range(10))
print(lista7) # = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista8 = list("Curso de Python")
print(lista8)

# elemento = 8 # verificar se está dentro da lista7 e lista8
elemento = int(input("Digite um elemento: "))  # Solicita ao usuário para inserir um elemento

if elemento in lista7:
  print("Este elemento está dentro da lista")
else:
  print("Este elemento não está na lista")