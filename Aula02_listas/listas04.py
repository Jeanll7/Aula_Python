import sys
sys.stdout.reconfigure(encoding='utf-8')

# index         01234
nome_planeta = "terra"

print(nome_planeta[2:4]) # = rr

# list2 = [2, 3, 5, 6, 8, 10]
# print(list2)

# list3 = [2.0, 3.5, 4.2]
# print(list3)

# join_list = list2 + list3
# print(f"A união das duas listas é {join_list}")

list1 = [2.0, 3.5, 4.7]
# print(list1)

list2 = [1, 5, 9, 11, 15]
# print(len(list2))

# index     0       1          2
list3 = ["Nome", "Idade", "Telefone"]
print(list3)

print(len(list1)) # = 3
print(len(list2)) # = 5
print(f"Total de numeros nas duas listas é", len(list1) + len(list2)) # = 8
print(sum(list1)) # soma 10.2
print(max(list1)) # retorna o elemento de valor máximo 4.7
print(max(list2)) # retorna o elemento de valor máximo 15
print(min(list1)) # retorna o elemento de valor mínimo 15
print(min(list2)) # retorna o elemento de valor mínimo 1



