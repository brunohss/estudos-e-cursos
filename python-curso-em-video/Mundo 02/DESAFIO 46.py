#Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o 
#estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.


from time import sleep


print('\n\033[0;33m====== DESAFIO 46 ======\033[m')
print('Contagem regressiva')
for c in range(10,-1,-1):
    print(f'\033[0;{27+c}m {c}')
    sleep(0.5)
print('Fim')