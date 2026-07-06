print('\033[0;33m====== DESAFIO 19 ======\033[m')
import random

na=input('digite o nome do primeiro : ')
nb=input('digite o nome do segundo  : ')
nc=input('digite o nome do terceiro : ')
print(f'O sorteiro o nome que foi sorteado foi : {random.choice([na,nb,nc])}')