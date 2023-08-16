# Escreva um programa para calcular as somas:
# Soma = 3/40 + 32 /39 + 33 /38 + 34 /37 + 340/1
# Soma = 480/2 + 475/22 + 470/23 + 465/24 + 460/25 + (20 primeiros termos)
# Soma = 1/2 + 3/23 + 7/25 + 15/27 + 31/29 + (15 primeiros termos)

def calcular_soma(numeradores, denominadores):
  soma = 0
  for i in range(len(numeradores)):
    soma += numeradores[i] / denominadores[i]
  return soma

# Soma 1
numeradores1 = [3, 32, 33, 34, 340]
denominadores1 = [40, 39, 38, 37, 1]
soma1 = calcular_soma(numeradores1, denominadores1)

# Soma 2
numeradores2 = [480, 475, 470, 465, 460]
denominadores2 = [2, 22, 23, 24, 25]
soma2 = calcular_soma(numeradores2, denominadores2)

# Soma 3
numeradores3 = [1, 3, 7, 15, 31]
denominadores3 = [2, 23, 25, 27, 29]
soma3 = calcular_soma(numeradores3, denominadores3)

print(f"Soma 1: {soma1:.6f}")
print(f"Soma 2: {soma2:.6f}")
print(f"Soma 3: {soma3:.6f}")