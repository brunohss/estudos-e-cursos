print('\033[0;33m====== DESAFIO 28 ======\033[m')
import random

num=int(input('Tenta a divinhar o numero que o computador pensou de 0 a 5.\n Digite o numero : '))
numpc=int(random.randrange(0,5,1))
if num==numpc:
    print('Vc acertou o numero')
else:
    print(f'O pc pensou no numero {numpc} e vc pensou digitou {num}')