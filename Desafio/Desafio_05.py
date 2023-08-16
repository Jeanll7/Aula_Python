# Encontrar a sequência de Fibonacci até o enésimo termo.

def fibonacci(n):
  fib = [0, 1]
  for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
  return fib

N = int(input("Digite um valor para N: "))
fib_sequence = fibonacci(N)
print(f"A sequência de Fibonacci com {N} termos é:", fib_sequence)

