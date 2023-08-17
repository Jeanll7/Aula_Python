import sys
sys.stdout.reconfigure(encoding='utf-8') 

# copia da lista

lista = ['a', 'b', 'c']
print(lista)

lista2 = lista.copy()
print(lista2)

lista2.append('d')
lista.append('e')

print(lista)
print(lista2)








  
  




