import sys
sys.stdout.reconfigure(encoding='utf-8') 

infos = [
  "João",
  "Paulo",
  "Brasil",
  "Solteiro",
  "Ensino Superior",
  "25",
]

nome, sobrenome, *_, escolaridade, idade = infos
print(f"{nome} {sobrenome} tem {escolaridade} e idade {idade} anos")