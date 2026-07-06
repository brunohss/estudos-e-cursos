print('\033[0;33m====== DESAFIO 15 ======\033[m')
dias=int(input('Digite os dias que ficou com o carro: '))
km=float(input('Digite quantos kms que andou com o carro:'))
print(f'Vc tera que pagar:\n {dias:2} Diarias x R$ 60,00/dia = R$ {dias*60:>6.2f} \n {km:4} Km x R$ 0,15/km      = R$ {km*0.15:>6.2f}\n TOTAL','-'*19,f'= R$ {dias*60+km*0.15:>6.2f}')