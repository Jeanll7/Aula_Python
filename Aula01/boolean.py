# and(e) | or(ou) | not(negação)

# Informações do aluno
gpa = 3.7
family_income = 25000  # Em dólares

# Defina os critérios da bolsa
minimum_gpa = 3.5
maximum_income = 30000  # Em dólares

# Verifique se o aluno é elegível para a bolsa
is_eligible = (gpa >= minimum_gpa) and (family_income <= maximum_income)

# Definir a codificação do console para UTF-8
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Exibir o resultado
if is_eligible:
    print("Parabéns!\n Você é elegível para a bolsa de estudos.")
else:
    print("Desculpe, você não atende aos critérios para a bolsa.")
