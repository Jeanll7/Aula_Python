import sys
sys.stdout.reconfigure(encoding='utf-8') 


dados = {"nome" : "Gabriel", "ano" : "1993", "valor_logico" : True}
dados.update({"estado":"Santa Catarina"}) 
print(dados) 

dicio = dados.copy()
print(dicio)

dicio2 = dict(dados)
print(dicio2)

dados["idade"] = 27
print(dados)
print(dicio)
print(dicio2)



  













  
  




