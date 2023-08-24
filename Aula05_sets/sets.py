import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Criando um conjunto com elementos
conjunto = {1, 2, 3, 4, 5}

print("Meu conjunto:", conjunto) # Exibindo o conjunto

print("3 está no conjunto:", 3 in conjunto) # Verificando se um elemento está no conjunto

conjunto.add(6) # Adicionando um elemento ao conjunto

conjunto.remove(4) # Removendo um elemento do conjunto

print("Meu conjunto atualizado:", conjunto) # Exibindo o conjunto atualizado

set1 = {4, 6, 7, 9, 1, 8}

set1.update([1, 4, 9, 10, 7]) # não repete o mesmo elemento
print(set1)


















  
  




