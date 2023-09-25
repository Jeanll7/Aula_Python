import os

"""os.mknod("olamundo.py")
os.makedirs("nova_pasta")
os.mknod("./nova_pasta/teste.txt")"""

# Nome do arquivo que você deseja criar
nome_arquivo = 'caminho_arquivo/renomear.py'

# Abra o arquivo para criação (ou substituição se já existir)
with open(nome_arquivo, 'w') as arquivo:
  pass

print(f'O arquivo {nome_arquivo} foi criado com sucesso.')


# os.rename("caminho_arquivo/renomear.py", "caminho_arquivo/renomeado.py")
