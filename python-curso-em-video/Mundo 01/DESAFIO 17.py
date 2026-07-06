print('\033[0;33m====== DESAFIO 17 ======\033[m')
import math
co=float(input('digite o valor do cateto oposto: '))
ca=float(input('digite o valor do cateto adjacente: '))
print(f'O valor da hipotenusa: {math.hypot(co,ca)}')