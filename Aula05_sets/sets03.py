import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Remover elementos com remove e discard
conjunto = {1, 2, 3} 

conjunto.remove(2)  # Remove o elemento 2 do conjunto
"""conjunto.remove(4)  # Isso gerará um erro KeyError, pois 4 não existe no conjunto"""

conjunto.discard(2)  # Remove o elemento 2 do conjunto
conjunto.discard(4)  # Não gera erro, pois 4 não existe no conjunto

print(conjunto)


















  
  




