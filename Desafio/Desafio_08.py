# Geração de Números Aleatórios e Ordenação

# random_numbers = random.sample(range(1, 61), 6)
# random_numbers.sort()  # clean_code

import random 

random_numbers = [] 
for _ in range(6): 
  while True: 
    number = random.randint(1, 60) 
    if number not in random_numbers: 
      random_numbers.append(number) 
      break 
  
random_numbers.sort() 

print(f"Os 6 números aleatórios são: {random_numbers}")  


