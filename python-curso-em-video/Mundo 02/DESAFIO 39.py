#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, 
# e acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata 
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo 
# que falta ou que passou do prazo
from datetime import date
print('\033[0;33m====== DESAFIO 39 ======\033[m')

hoje =int (date.today().year)
NumA=int(input('Digite o ano do seu nascimento:'))
if NumA +18 < hoje: print(f'Voce tem {hoje-NumA} de idade e ja passou {hoje-NumA-18} anos da idade de se alistar')
elif NumA +18 > hoje: print(f'Voce tem {hoje-NumA}anos de idade e ainda tera que esperar {NumA+18-hoje} anos para se alistar')
else: print('Este ano é o ano para se alistar')