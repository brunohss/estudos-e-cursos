# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

#– O primeiro valor é maior

#– O segundo valor é maior

#– Não existe valor maior, os dois são iguais

print('\033[0;33m====== DESAFIO 38 ======\033[m')


NumA=int(input('Digite um numero:'))
NumB=int(input('Digite outro numero:'))
print (f'Numeros Iguais' if NumA==NumB else f'O primeiro numero: {NumA} menor que o segundo: {NumB}'if NumA>NumB else f'O segundo numero: {NumB} maior que o primeiro: {NumA}')