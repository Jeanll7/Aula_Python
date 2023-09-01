import sys
sys.stdout.reconfigure(encoding='utf-8') 

"""02 - Escreva uma função de potenciação, em que os dados de entrada são: base e
expoente (inteiros)."""

def exponentiation(base, exponent):
  result  = 1
  
  if exponent < 0:
    base = 1 / base
    exponent = -exponent
    
  for _ in range(exponent):
    result  *= base
  return result 

base = 2
exponent = 2
result  = exponentiation(base, exponent)
print(f"{base} elevado a {exponent} é igual a {result}")

# ============================================================

def exponentiation(base, exponent):
  result = 1

  if exponent < 0:
    print("Sorry, this function does not handle negative exponents.")
    return None

  for i in range(exponent):
    result *= base
  return result

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent (a non-negative integer): "))

if exponent >= 0:
  result = exponentiation(base, exponent)
  if result is not None:
    print(f"{base} raised to the power of {exponent} is equal to {result}")







