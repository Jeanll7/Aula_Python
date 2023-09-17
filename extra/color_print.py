# from colorama import init, Fore, Back

# init()

# print(Fore.GREEN + "Texto em verde")
# print(Back.BLUE + "Fundo em azul")

from colorama import init, Fore, Back

init()

cor_texto = Fore.WHITE
fundo = Back.YELLOW

texto = " Texto com cor e fundo "

# Imprima o texto com a cor e o fundo definidos
print(cor_texto + fundo + texto )
