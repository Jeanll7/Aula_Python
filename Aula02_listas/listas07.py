import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Mudando de itens

# index    0          1         2        3          4         5
lista = ['gato', 'cachorro', 'peixe', 'cavalo', 'tubarão', 'girafa']
print(lista)

# print(type(lista))
# print(lista[1])
# # lista[1] = 'leão'

# lista[1:4] = ['águia', 'macaco', 'elefante']
# print(lista)

lista[1:5] = ['tubarão']
print(lista)
print(len(lista))
