import sys
sys.stdout.reconfigure(encoding='utf-8') 

# index     0        1        3
lista = ["item2", "item3", "item2"]
tupla = ("item2", "item3", "item2")

# chave: valor
dados = {"nome" : "Gabriel", "ano" : "1993", "valor_logico" : True}
dados.update({"estado":"Santa Catarina"})
print(dados)

# A função popitem elimina o último item apenas da versão 3.7 e acima
dados.popitem() 
print(dados)

dados.pop("nome") # elimina um item específico
print(dados)













  
  




