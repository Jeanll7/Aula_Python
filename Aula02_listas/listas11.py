import sys
sys.stdout.reconfigure(encoding='utf-8') 

# ordenar nomes e colacar a primeira letra em maiúscula

def capitalize_first_letters(lst):
  new_list = [word.capitalize() for word in lst]
  return new_list

lista = ['Ana', 'Pedro', 'Marta', 'Clara', 'beatriz', 'ana clara', 'jorge']
print(lista)

lista = capitalize_first_letters(lista)
lista.sort(key=str.lower)
print(lista) # = ['Ana', 'Ana clara', 'Beatriz', 'Clara', 'Marta', 'Pedro']







  
  




