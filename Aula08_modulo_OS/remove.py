import sys
sys.stdout.reconfigure(encoding='utf-8') 

import os

# Especifique o caminho completo do arquivo que você deseja remover
caminho_arquivo = '/Jean/Curso_Python/Python/caminho_arquivo/teste.py'

# Verifique se o arquivo existe antes de tentar removê-lo
if os.path.exists(caminho_arquivo):
  # Remove o arquivo
  os.remove(caminho_arquivo)
  print(f"O arquivo {caminho_arquivo} foi removido com sucesso.")
else:
  print(f"O arquivo {caminho_arquivo} não existe.")
