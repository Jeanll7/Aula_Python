import sys
sys.stdout.reconfigure(encoding='utf-8') 

# Fatorial sem recursão 

def factorial(n):
  if n == 0:
    return 1

  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

number = 5
result = factorial(number)
print(f'O fatorial de {number} é {result}')

# code clean
"""number = 5
result = 1

for i in range(1, number + 1):
  result *= i

print(f'O fatorial de {number} é {result}')"""

# Fatorial solução recursiva

def factorial_recursive(number):
  if number == 0:
    return 1
  else:
    return number * factorial_recursive(number - 1)
    
number = 5
result = factorial_recursive(number)
print(f'O fatorial de {number} é {result}')





