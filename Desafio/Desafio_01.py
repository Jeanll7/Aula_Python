# Normalmente, quando você compra algo, é perguntado se o número do seu cartão de crédito, número de telefone ou resposta à sua pergunta mais secreta ainda está correto. No entanto, como alguém pode olhar por cima do seu ombro, você não quer que isso apareça na tela. Em vez disso, nós o mascaramos.
# Sua tarefa é escrever uma função maskify, que transforma todos, exceto os últimos quatro caracteres, em '#'.


def maskify(cc):
  # Verifica se o número é menor ou igual a 4 caracteres
  if len(cc) <= 4:
    return cc
  else:
    # Mascara todos os caracteres, exceto os últimos 4
    return '#' * (len(cc) - 4) + cc[-4:]

print(maskify("48854454"))

print(20 * "-")

def maskify(cc):
  return "#" * (len(cc)-4) + cc[-4:]

print(maskify("48845"))