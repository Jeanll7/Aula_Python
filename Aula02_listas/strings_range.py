import sys
sys.stdout.reconfigure(encoding='utf-8')


# Comentário do meu código

###    "0123456"
nome = "Chicago"

print(nome[0]) # Letra C

for x in range(1, 11, 1):
  print(x)
  
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

print("-----------------")
  
for x in range(10, 0, -1):
  print(x)
  
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

nome = "chicago"
nome2 = "queens"

print(nome, end=" ")
print(nome2)

nome = "chicago"

for x in nome:
  print(x, end="_")   

x = 5 
y = 0

x, y = y, x # troca de variável

print(x)
print(y) 

a = 5
b = 10

a, b = b, a # troca de variável

print("a:", a)
print("b:", b)