import sys
sys.stdout.reconfigure(encoding='utf-8') 

# concatenando listas

"""lista = ['a', 'b', 'c']
lista2 = [1, 4, 6]"""

"""lista += lista2
print(lista)"""

"""lista.extend(lista2)
print(lista)"""

# lista = ['a', 'b', 'c']
# lista2 = [1, 4, 6]

# # string primeiro, depois números
# nova_lista = lista + [item for item in lista2]
# print(nova_lista)

# # números primeiro, depois string
# for index, item in enumerate(lista2):
#   lista.insert(index, item)

# print(lista) 


lista = ['a', 'b', 'c']
lista2 = [1, 4, 6]
lista3 = [8, 12, 16]

# for x in lista3:
for x in lista2:
  lista.append(x)
print(lista)




  
  




