import sys
sys.stdout.reconfigure(encoding='utf-8') 

# index     0        1        3
lista = ["item2", "item3", "item2"]
tupla = ("item2", "item3", "item2")

# chave: valor
dados = {"nome" : "Gabriel", "ano" : "1993", "valor_logico" : True}
dados.update({"estado":"Santa Catarina"})
print(dados)

for chave in dados:
  print(chave) 

print("----"*10)

for chave in dados:
  print(dados[chave])
  
print("----"*10)
  
for chave in dados.values():
  print(chave)
  
print("----"*10)
  
for chave in dados.keys():
  print(chave)
  














  
  




