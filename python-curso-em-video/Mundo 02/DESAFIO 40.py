#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

from datetime import date
print('\033[0;33m====== DESAFIO 40 ======\033[m')

NumA=float(input('Digite a primeira nota:'))
NumB=float(input('Digite a segunda nota:'))
if (NumA+NumB)/2 < 5.0: print(f'Sua média foi: {(NumA+NumB)/2}\nVoce Foi reprovado')
elif (NumA+NumB)/2 > 7.0: print(f'Sua média foi: {(NumA+NumB)/2}\nVoce foi aprovado')
else: print(f'Sua média foi: {(NumA+NumB)/2}\nVoce está de recuperação')