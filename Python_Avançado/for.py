import sys
sys.stdout.reconfigure(encoding='utf-8') 

produtos = [
  'iphone',
  'ipad',
  'airpod',
  'macbook',
]
  
for i in range(len(produtos)):
  print(i, produtos[i])

# ========================================================================

# forma certa
for i, item in enumerate(produtos):
  print(i, item)
  
  