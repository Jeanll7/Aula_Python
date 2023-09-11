import sys
sys.stdout.reconfigure(encoding='utf-8') 

# import random
# import random import choice

"""from random import (  
  random,
  choice
)"""

import random as rd

print(rd.random())

numero_aleatorio = rd.random()
numero_formatado = "{:.6f}".format(numero_aleatorio).replace(".", "").lstrip("0")
print(numero_formatado)


    


















  
  




