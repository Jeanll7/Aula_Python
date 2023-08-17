import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Criando um dicionário com informações de uma pessoa
pessoa = {
  "nome": "João",
  "idade": 30,
  "cidade": "São Paulo"
}

# Acessando valores usando as chaves
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Adicionando um novo item ao dicionário
pessoa["profissao"] = "Engenheiro"

# Modificando um valor existente
pessoa["idade"] = 31

# Removendo um item do dicionário
del pessoa["cidade"]

# Imprimindo o dicionário completo
print(pessoa)












  
  




