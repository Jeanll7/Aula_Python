# Converter uma temperatura em Fahrenheit para Celsius.

def fahrenheit_para_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = fahrenheit_para_celsius(fahrenheit)
print(f"{fahrenheit:.2f}°F é equivalente a {celsius:.2f}°C")


