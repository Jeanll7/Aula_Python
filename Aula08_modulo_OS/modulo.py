import sys
sys.stdout.reconfigure(encoding='utf-8') 

import os 

# print(os.name)  
print(os.path.exists('config.txt'))
print(os.path.exists('teste.txt'))

# criando um diretório
# os.mkdir('teste')

# Caminho completo para o arquivo
# caminho_arquivo = '/Jean/Curso_Python/Python/novapasta/teste.py'

# # Abra o arquivo para escrita (ou cria um novo arquivo se ele não existir)
# with open(caminho_arquivo, 'w') as arquivo:
#   pass  

import os

# Caminho completo para o arquivo
"""caminho_arquivo = '/Jean/Curso_Python/Python/olamundo.py'

# Abra o arquivo para escrita (ou cria um novo arquivo se ele não existir)
with open(caminho_arquivo, 'w') as arquivo:
    pass  # O arquivo está vazio, pois não estamos escrevendo nada nele neste exemplo"""


# Abra um arquivo para escrita (ou cria um novo arquivo se ele não existir)
with open('./compras.txt', 'w') as arquivo:
    pass  # O arquivo está vazio, pois não estamos escrevendo nada nele neste exemplo



