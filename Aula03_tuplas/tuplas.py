import sys
sys.stdout.reconfigure(encoding='utf-8') 

# As tuplas são imutáveis, enquanto as listas são mutáveis.

lista = ["item1", "item2", "item3"]

print(lista)
print(len(lista))
print(type(lista))
print("----"*10)

# index     0        1        2        3        4
tupla = ("item1", "item2", "item3", "item1", "item1")

print(tupla)
print(len(tupla))
print(type(tupla))
print(tupla[2])

print(tupla.count('item1'))












  
  




