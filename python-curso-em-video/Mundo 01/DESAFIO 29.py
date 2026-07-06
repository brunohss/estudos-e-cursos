print('\033[0;33m====== DESAFIO 29 ======\033[m')
vel=float(input('Digite a Velocidade do Carro em Km: '))
if vel>80:
    print(f'Voce foi multado no valor de : R$ {(vel-80)*7:.2f}')
else:
    print(f'Voce nao foi multado')