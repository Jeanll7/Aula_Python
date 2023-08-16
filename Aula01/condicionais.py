# Definir a codificação do console para UTF-8
import sys
sys.stdout.reconfigure(encoding='utf-8')

# if , else , (elif) -> (else if)  

# x = 3
# y = 3

# if y > x:
#   print('y é maior do que x')
#   print('Código dentro do bloco condicional if')
# elif y < x:
#   print('Código dentro do bloco condicional elif')
#   print('y é menor do que x')
# else:
#   print('x é igual a y')
  
# print('Código fora do bloco condicional')

# a = 5
# b = 8

# if a > b: print("b é maior que a")
# print("código fora do if")

# print("B") if b < a else print("A")

a = 12
b = 8
c = 2

if a > b:
  if a > c:
    print("A é maior que b e c")

