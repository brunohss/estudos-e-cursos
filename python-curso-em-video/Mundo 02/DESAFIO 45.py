#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
#considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros

from random import randint
print('\n\033[0;33m====== DESAFIO 45 ======\033[m')
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
jogador = int(input('''Suas Opções:
1) Pedra 
2) Papel 
3) Tesoura
Qual a sua jogada?'''))
jogador-1
print('-='*11)
print (f'O Jogador escolheu {itens[jogador]}')
print (f'O computador escolheu {itens[computador]}')
print('-='*11)
if computador  ==0: 
    if jogador   ==0:print('Vc Empate')
    elif jogador == 1:print('Vc Ganhou')
    else:print('Vc Perdeu')
elif computador ==1:
    if jogador   ==0:print('Vc Perdeu')
    elif jogador == 1:print('Vc Empatou')
    else:print('Vc Ganhou')
else:
    if jogador   ==0:print('Vc Ganhou')
    elif jogador == 1:print('Vc Perdeu')
    else:print('Vc Empatou')