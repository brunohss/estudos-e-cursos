#Exercício Python 50: Desenvolva um programa que leia seis números inteiros 
#e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.



print('\n\033[0;33m====== DESAFIO 49 ======\033[m')
print('Digite 6 numeros é sera somado somente os pares')
par=0
impar=0
for c in range(1,7,1):
    n1 =int(input(f'digite o numero {c}: '))
    if n1%2==0:par+=n1
    else: impar+=n1

 
print(f'Total da soma do pares: \033[0;34m {par}')
print(f'\033[mTotal da soma do impares: \033[0;34m {impar}')