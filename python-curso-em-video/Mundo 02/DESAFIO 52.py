#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 



print('\n\033[0;33m====== DESAFIO 52 ======\033[m')
print('Programa para saber se é primo ou nao')
n1 =int(input(f'digite o numero: '))
divisores =[]
for c in range(n1,0,-1):
    
    if n1%c==0:divisores.append(c)

 
print(f'Total de divisores: \033[0;32m {len(divisores)}\033[m')
print(f'Os divisores são: \033[0;32m {divisores}\033[m')
print(f'\033[0;32mO numero é Primo' if len(divisores)==2 else '\033[0;35mO numero não é Primo')