import sys
sys.stdout.reconfigure(encoding='utf-8')

# Objetos Dunder

class MinhaClasse:
  def __init__(self, valor):
    """
    Este é o método dunder __init__.
    É chamado quando um objeto da classe é criado.
    """
    self.valor = valor

  def __str__(self):
    """
    Este é o método dunder __str__.
    Define a representação em string do objeto.
    """
    return f'Objeto MinhaClasse com valor: {self.valor}'

  def __len__(self):
    """
    Este é o método dunder __len__.
    Define o comportamento da função len() para o objeto.
    """
    return len(self.valor)

  def __getitem__(self, indice):
    """
    Este é o método dunder __getitem__.
    Permite que o objeto seja indexado como uma sequência.
    """
    return self.valor[indice]

  def __setitem__(self, indice, novo_valor):
    """
    Este é o método dunder __setitem__.
    Permite atribuir valores a elementos do objeto como uma sequência.
    """
    self.valor[indice] = novo_valor

  def __iter__(self):
    """
    Este é o método dunder __iter__.
    Torna o objeto iterável, permitindo um loop for.
    """
    return iter(self.valor)

# Criando um objeto da classe
objeto = MinhaClasse([1, 2, 3, 4, 5])

# Usando métodos dunder
print(objeto)  # Chama __str__
print(len(objeto))  # Chama __len__
print(objeto[2])  # Chama __getitem__
objeto[2] = 6  # Chama __setitem__
for elemento in objeto:  # Chama __iter__
  print(elemento)
