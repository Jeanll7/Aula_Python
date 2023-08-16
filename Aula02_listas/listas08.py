import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Mudando de itens

# index     0        1        2       
# lista = ['carro', 'barco', 'avião']
# print(lista)

# for x in range(len(lista)):
  # print(x + 1, lista[x]) # = 1 carro, 2 barco, 3 avião
  # print(x, lista[x]) # = 0 carro, 1 barco, 2 avião
  
# texto = 'carro, avião'
# lista2 = list(texto)
# print(lista2)  

# texto = texto.split()
# texto = texto.split(',')
# print(texto)

# index     0        1        2       
lista = ['carro', 'barco', 'avião']
print(lista)

lista.append('moto')
lista.append('moto', 'navio', 'bicicleta') # erro: leva exatamente um argumento

print(lista)
print(len(lista)) # 4 elementos = lista.append('moto')   

for x in range(len(lista)):
  print(x, lista[x])
  



  
  




