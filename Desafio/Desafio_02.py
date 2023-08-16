# Retorna o número (contagem) de vogais na string fornecida.
# Consideraremos a, e, i, o, u como vogais para este Kata (mas não y).
# A string de entrada consistirá apenas em letras minúsculas e/ou espaços.

def get_count(sentence):
  vowels = "aeiouAEIOU"  
  vowels_count = 0  

  for char in sentence:  
    if char in vowels:  
      vowels_count += 1  

  return vowels_count  


# def getCount(inputStr):
#   return sum(1 for let in inputStr if let in "aeiouAEIOU")

