import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Argumentos Nomeados

"""def imprimir_nome(nome, sobrenome, idade):
  print("nome: ", nome)
  print("sobrenome: ", sobrenome)
  print("idade: ", idade)

nome = "João"
sobrenome = "Silva"
idade = 30

imprimir_nome(nome=nome, sobrenome=sobrenome, idade=idade)
print("-"*30)"""

# Parâmetro Padrão

def imprimir_imovel(nome_imovel, numeros_quartos, vaga_garagem=None): 
  print("Título:", nome_imovel)
  print("Quartos:", numeros_quartos)
  
  if vaga_garagem is not None:
    print("Vagas na garagem:", vaga_garagem)
    
    
imprimir_imovel("Casa na Praia", 3)  # Sem vaga na garagem
imprimir_imovel("Apartamento no Centro - Florianópolis", 2, 1) # 1 vagas na garagem

 




