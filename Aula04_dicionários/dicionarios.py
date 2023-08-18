import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Criando um dicionário com informações de um carro
carro = {
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2020,
  "cor": "Prata"
}

# Acessando valores usando as chaves
print("Marca:", carro["marca"])
print("Modelo:", carro["modelo"])
print("Ano:", carro["ano"])
print("Cor:", carro["cor"])

# Adicionando um novo item ao dicionário
carro["quilometragem"] = 15000

# Modificando um valor existente
carro["ano"] = 2021

# Imprimindo o dicionário atualizado
print(carro)
















  
  




