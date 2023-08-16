import sys
sys.stdout.reconfigure(encoding='utf-8')

numero = int(input("Digite um numero: "))

if numero > 0:
  print(f"O {numero} é possitivo ")
elif numero == 0:
  print(f"O {numero} é igual a zero")
else:
  print(f"O {numero} é negativo")