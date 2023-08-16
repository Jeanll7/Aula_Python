# Definir a codificação do console para UTF-8
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Área de um retângulo

base = float(input("Qual o tamanho da base do seu retangulo?"))
altura = float(input("Qual o tamanho da altura do seu retangulo?"))
area = base * altura
print(f'O seu retangulo possui area: {area} unudades de medida')

# 2. Área de um quadrado

lado = float(input("Digite o lado do quadrado: "))
area = lado ** 2
print(f"A área do quadrado é {area}")

# 3. Cálculo de desconto em um produto

valor_produto = float(input("Digite o valor do produto em reais: "))
desconto_percentual = float(input("Digite o valor do desconto em porcentagem: "))
valor_com_desconto = valor_produto - (valor_produto * (desconto_percentual / 100))
print(f"O valor do produto com desconto é R${valor_com_desconto}")

# 4. Área de um círculo (usando pi = 3.14592)

raio = float(input('Digite o raio do círculo: '))
area = 3.14592 * raio ** 2
print(f"A área do círculo é {area}")

# 5. Conversão de Reais para Dólares

taxa_cambio = float(input("Digite a taxa de câmbio atual (Reais para Dólares): "))
valor_em_reais = float(input("Digite o valor em Reais: "))
valor_em_dolares = valor_em_reais / taxa_cambio
print(f"O valor em Dólares é {valor_em_dolares}")

# 6. Conversão de Dólares para Reais

taxa_cambio = float(input("Digite a taxa de câmbio atual (Dólares para Reais): "))
valor_em_dolares = float(input("Digite o valor em Dólares: "))
valor_em_reais = valor_em_dolares * taxa_cambio
print(f"O valor em Reais é {valor_em_reais}")