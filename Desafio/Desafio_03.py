# Escreva um programa que leia 5 valores e encontre o maior e o menor deles. Mostre o
# resultado.
# Análise:
# Eu poderia supor que o menor fosse um número pequeno qualquer (ou que o maior
# fosse um número grande) ao invés de, inicialmente, supor que ele fosse o primeiro?
# Resposta: Não!
# Exemplo: Suponha que fosse atribuído à variável menor o valor -500 e que o
# usuário digitasse apenas valores maiores que -500 (exemplo: -10, -9, 0, 6, 7 e 450),
# se o valor armazenado na variável menor nunca for trocado, a suposição estaria
# incorreta - erro de lógica - pois o valor supostamente menor estaria fora do conjunto
# dos valores digitados e, portanto, válidos). O mesmo raciocínio vale para maior
# Solução: Supor que as variáveis maior e menor assumam o valor do primeiro
# elemento digitado, fora da estrutura de repetição. Assim, no caso do menor
# elemento, ao comparar o valor atualmente armazenado nesta variável com os
# demais elementos digitados (do 2º em diante) ele poderá ser alterado (ou não, caso
# o menor de todos os valores digitados seja efetivamente o primeiro). De igual forma,
# o valor da variável maior poderá ser alterado, caso haja entre os números
# posteriormente digitados um valor maior que o considerado o maior até então.


numeros = []  # Cria uma lista vazia para armazenar os valores inseridos.
for _ in range(5):  # Loop para repetir o processo de entrada cinco vezes.
  valor = float(input("Digite um valor: "))  # Solicita ao usuário um valor e converte para ponto flutuante.
  numeros.append(valor)  # Adiciona o valor à lista "numeros".

maior = menor = numeros[0]  # Inicializa as variáveis "maior" e "menor" com o primeiro valor da lista.

for numero in numeros:  # Loop para iterar sobre cada número na lista "numeros".
  if numero > maior:  # Verifica se o número atual é maior que o valor armazenado em "maior".
    maior = numero  # Se for, atualiza o valor de "maior".
  if numero < menor:  # Verifica se o número atual é menor que o valor armazenado em "menor".
    menor = numero  # Se for, atualiza o valor de "menor".

print(f"O maior valor é: {maior}")  # Imprime o maior valor encontrado.
print(f"O menor valor é: {menor}")  # Imprime o menor valor encontrado.
