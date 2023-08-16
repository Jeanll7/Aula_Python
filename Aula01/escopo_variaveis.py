
x = 5 

def funcao():
    x = 3
    print("Valor da variavel local: " , x)
    
funcao()
print("Valor da variavel global: ", x)
  
# errado
y = 'Gabriel' #nome
z = 1.17 #altura
t = "000.000.000-00" #cpf
l = 23 #idade
 
# certo 
nome = "Gabriel"
altura = 1.74
cpf = "000.000.000-00"
idade = 23

# Exibição das informações da pessoa
print("Nome:", nome)
print("Altura:", altura, "m")
print("CPF:", cpf)
print("Idade:", idade, "anos")