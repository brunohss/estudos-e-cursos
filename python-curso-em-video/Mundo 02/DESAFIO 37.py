# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 
# 3 para hexadecimal. ara aprovar o empréstimo bancário 

print('\033[0;33m====== DESAFIO 37 ======\033[m')


Numero=int(input('Digite o numero:'))
Opção=int(input('Digite o valor do salario:qual será a base de conversão:\n1 para binário, 2 para octal e 3 para hexadecimal\n'))

if (Opção ==1):print(f'O numero em Binario é : {format(Numero,"b") }' " (bin)")
elif (Opção ==2): print(f'O numero em Octal é : {format(Numero,"o") }'" (oct)")
elif (Opção ==3): print(f'O numero em hexadecimal é : {format(Numero,"X") }'" (hex)")
else: print('Opção incorreta')