import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Ultilizando funções principais dos sets
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}

conjunto1.update(conjunto2)
print(conjunto1)

conjunto3 = {1, 5, 3, 2}
conjunto4 = {3, 6, 2}

conjunto3.intersection_update(conjunto4)
print(conjunto3)

conjunto8 = {1, 5, 3, 2}
conjunto9 = {3, 6, 2}

conjunto8.symmetric_difference_update(conjunto9)
print(conjunto8)





















  
  




