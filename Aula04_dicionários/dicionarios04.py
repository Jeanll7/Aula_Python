import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Criando um dicionário de nomes e chaves
dicionario = {
  "nome": "Bruna",
  "idade": "27",
  "nacionalidade": "brasileira",
  "idade": "35"
}

print(dicionario)
# print(dicionario["idade"])

print(dicionario.get('idade'))
print(dicionario.values())

if "idade45" in dicionario:
  print("A chave idade existe")
else:
  print('A chave não existe')
  
  
print(dicionario.items())
  
  
  
















  
  




