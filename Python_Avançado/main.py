import sys
sys.stdout.reconfigure(encoding='utf-8') 

dia = 3

dias_da_semana = {
  1: "Domingo",
  2: "Segunda-feira",
  3: "Terça-feira",
  4: "Quarta-feira",
  5: "Quinta-feira",
  6: "Sexta-feira",
  7: "Sábado"
}

dia_da_semana = dias_da_semana.get(dia, "Dia inválido")

print(dia_da_semana)

# ========================================================================

import datetime

dias_da_semana = [
  "Domingo",
  "Segunda-feira",
  "Terça-feira",
  "Quarta-feira",
  "Quinta-feira",
  "Sexta-feira",
  "Sábado"
]

data_atual = datetime.datetime.now()
dia_da_semana = dias_da_semana[data_atual.weekday()]

print("Data atual:", data_atual.strftime("%d-%m-%Y")) 
print("Dia da semana:", dia_da_semana)