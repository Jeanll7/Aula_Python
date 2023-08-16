import sys
sys.stdout.reconfigure(encoding='utf-8') 

# remover itens

# index     0        1        2       
lista = ['carro', 'barco', 'avião']
print(lista)

# lista.pop() # remove o ultimo elemento da lista
lista.pop(0) # remove o index específico (0)

lista.insert(1, 'moto') # = ['carro', 'moto', 'barco', 'avião']
# print(lista)

lista.remove('moto')
print(lista)

del lista[1] # remove o index específico (1)
print(lista)

for x in range(len(lista)):
  print(x, lista[x])






  
  




