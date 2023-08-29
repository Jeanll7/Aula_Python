import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Argumento Arbitrário  **Kwags

"""def imprimir_info(**kwargs):
  for chave, valor in kwargs.items():
    print(f"{chave}: {valor}")

imprimir_info(nome="Alice", idade=30, cidade="São Paulo")"""


def listar_produtos(**produtos):
  for produto, preco in produtos.items():
    print(f"Produto: {produto} - Preço: R$:{preco:.2f}")
    
produtos = {
  "Camiseta": 25.99,
  "Calça Jeans": 45.50,
  "Tênis": 79.99,
  "Mochila": 32.75
}

listar_produtos(**produtos)





 




