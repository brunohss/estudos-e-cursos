print('\033[0;33m====== DESAFIO 23 ======\033[m')
num=int(input('Digite o numero com o maximo 4 carateres: '))

print(f'Unidade  : {num//1%10}\nDezena   : {num//10%10}\nCentenas : {num//100%10}\nMilhar   : {num//1000}')
