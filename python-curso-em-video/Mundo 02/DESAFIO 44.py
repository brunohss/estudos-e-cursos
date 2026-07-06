#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
#considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros

print('\n\033[0;33m====== DESAFIO 44 ======\033[m')

valor=float(input('\nDigite o valor que ser pago:'))
modo=int(input('Formas de pagamento: \n \33[0;32m1)\33[m à vista dinheiro/cheque: 10%" de desconto\n \33[0;32m2)\33[m à vista no cartão: 5%" de desconto\n \33[0;32m3)\33[m em até 2x no cartão: preço formal\n \33[0;32m4)\33[m 3x ou mais no cartão: 20%" de juros que ira ser pago\n Digite a opção : '))
if   modo==1 : print(f'O valor que será pago R$ \33[0;34m{valor-valor/10:.2f}')
elif modo==2 : print(f'O valor que será pago R$ \33[0;34m{valor-valor/20:.2f}')
elif modo==3 : print(f'O valor que será pago R$ \33[0/34m{valor:.2f}')
elif modo==4 : print(f'O valor que será pago R$ \33[0;34m{valor+valor/5:.2f}')
else : print('\33[0;31mOpção incorreta\33[m ')