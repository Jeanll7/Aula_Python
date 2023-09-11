import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Objetos Dunder

class Pessoa:
  def __init__(self, nome):
    self.nome = nome

  def __str__(self):
    return f"Olá, meu nome é {self.nome}."

pessoa1 = Pessoa("Alice")
print(str(pessoa1))  
pessoa2 = Pessoa("Bob")
print(pessoa2)  





















  
  




