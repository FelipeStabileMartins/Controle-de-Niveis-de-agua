# Controle de Níveis de Água
# Felipe Stabile Martins

#Usando Lista 
niveis = [
"NÍVEL MUITO BAIXO (Crítico)",
"Nível baixo",
"Nível médio",
"Nível alto",
"NÍVEL MUITO ALTO (Alerta)"
]

#Usando Colorama para cores
from colorama import Fore, Style 
print()
print("Controle de Níveis de Água")
Nivel_agua = float(input("Digite o nível de água (1 a 5): "))
print()

print("Níveis de água ou Nível do reservatório:")
if Nivel_agua == 1:
    print(Fore.RED, niveis[0])
elif Nivel_agua == 2:
    print(Fore.YELLOW,niveis[1])
elif Nivel_agua == 3:
    print(Fore.GREEN, niveis[2])
elif Nivel_agua == 4:
    print(Fore.CYAN, niveis[3])
elif Nivel_agua == 5:
    print(Fore.BLUE, niveis[4])
else:
    print(Fore.MAGENTA,"Nível inválido! Digite um número de 1 a 5.")
print(Style.RESET_ALL)
print()