#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia 
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER

from datetime import date
print('\033[0;33m====== DESAFIO 41 ======\033[m')

hoje =int (date.today().year)
NumA=int(input('Digite o ano do seu nascimento:'))
if   hoje-NumA  <  9:  print(f'Voce tem {hoje-NumA} de idade e está na categoria: MIRIM')
elif hoje-NumA  < 14:  print(f'Voce tem {hoje-NumA} de idade e está na categoria: INFANTIL')
elif hoje-NumA  < 19:  print(f'Voce tem {hoje-NumA} de idade e está na categoria: JÚNIOR')
elif hoje-NumA  < 25:  print(f'Voce tem {hoje-NumA} de idade e está na categoria: SÊNIOR')
else:             print(f'Voce tem {hoje-NumA} de idade e está na categoria: MASTER')