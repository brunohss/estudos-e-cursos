#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.



print('\n\033[0;33m====== DESAFIO 48 ======\033[m')
print('todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500')
total = 0
for c in range(1,500,1):
    if c%3==0: total +=c


print(f'\033[0;34m {total}')