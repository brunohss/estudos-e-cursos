print('\033[0;33m====== DESAFIO 20 ======\033[m')
import random
n1=input('digite o nome do 1 aluno: ')
n2=input('digite o nome do 2 aluno: ')
n3=input('digite o nome do 3 aluno: ')
print(f'A ordem de apresentacao do trabalho sera: {random.sample([n1,n2,n3],k=3)}')